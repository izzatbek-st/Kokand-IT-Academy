"""Telegram admin bot for lead notifications and Excel downloads."""

from __future__ import annotations

from html import escape
from pathlib import Path
import json
import os
import tempfile
import time
import uuid
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from openpyxl import load_workbook


BOT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BOT_DIR.parent
ENV_FILE = PROJECT_DIR / '.env'
EXCEL_FILE = PROJECT_DIR / 'Lidlar.xlsx'
PENDING_LEADS_FILE = PROJECT_DIR / 'pending_leads.json'
OUTBOX_DIR = PROJECT_DIR / 'telegram_outbox'
EXCEL_BUTTON = 'Excel'


def load_settings():
    if not ENV_FILE.exists():
        raise RuntimeError('.env file was not found.')

    settings = {}
    for line in ENV_FILE.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        settings[key.strip()] = value.strip().strip('"').strip("'")

    token = settings.get('TELEGRAM_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN')
    admin_chat_id = settings.get('TELEGRAM_ADMIN_CHAT_ID') or os.getenv('TELEGRAM_ADMIN_CHAT_ID')
    if not token or not admin_chat_id:
        raise RuntimeError('Bot token or admin chat ID is missing.')
    return token, str(admin_chat_id)


def telegram_request(method, payload, timeout=15):
    token, _ = load_settings()
    request = Request(
        f'https://api.telegram.org/bot{token}/{method}',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    with urlopen(request, timeout=timeout) as response:
        result = json.loads(response.read().decode('utf-8'))
    if not result.get('ok'):
        raise RuntimeError(f'Telegram rejected {method}.')
    return result['result']


def send_message(chat_id, text, show_keyboard=False, parse_mode=None):
    payload = {'chat_id': chat_id, 'text': text}
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if show_keyboard:
        payload['reply_markup'] = {
            'keyboard': [[EXCEL_BUTTON]],
            'resize_keyboard': True,
            'is_persistent': True,
        }
    telegram_request('sendMessage', payload)


def send_lead_message(lead):
    _, admin_chat_id = load_settings()
    message = (
        '<b>Yangi royxatdan otish</b>\n\n'
        f'<b>Ism:</b> {escape(str(lead.get("name", "-")))}\n'
        f'<b>Telefon:</b> {escape(str(lead.get("phone", "-")))}\n'
        f'<b>Kurs:</b> {escape(str(lead.get("course", "-")))}\n'
        f'<b>Izoh:</b> {escape(str(lead.get("note") or "-"))}\n'
        f'<b>Vaqt:</b> {escape(str(lead.get("submitted_at", "-")))}'
    )
    send_message(admin_chat_id, message, parse_mode='HTML')


def process_outbox():
    """Deliver saved website requests. Failed records stay in the outbox."""
    OUTBOX_DIR.mkdir(exist_ok=True)
    for message_file in sorted(OUTBOX_DIR.glob('*.json')):
        try:
            lead = json.loads(message_file.read_text(encoding='utf-8'))
            if not isinstance(lead, dict):
                raise ValueError('Invalid lead record.')
            send_lead_message(lead)
            message_file.unlink()
        except (OSError, ValueError, json.JSONDecodeError, RuntimeError, HTTPError, URLError, TimeoutError) as error:
            print(f'Lead delivery failed: {error}')
            break


def create_excel_export():
    """Include pending leads if the original workbook is still open in Office."""
    if not PENDING_LEADS_FILE.exists():
        return EXCEL_FILE, False
    try:
        pending_leads = json.loads(PENDING_LEADS_FILE.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        pending_leads = []
    if not pending_leads:
        return EXCEL_FILE, False

    workbook = load_workbook(EXCEL_FILE)
    worksheet = workbook.active
    for lead in pending_leads:
        worksheet.append([
            lead.get('name', ''),
            lead.get('phone', ''),
            lead.get('course', ''),
            lead.get('note', ''),
            lead.get('submitted_at', ''),
        ])

    file_descriptor, temporary_path = tempfile.mkstemp(prefix='Lidlar-', suffix='.xlsx')
    os.close(file_descriptor)
    export_file = Path(temporary_path)
    workbook.save(export_file)
    return export_file, True


def send_excel(chat_id):
    if not EXCEL_FILE.exists():
        send_message(chat_id, 'Hozircha royxatlar fayli mavjud emas.')
        return

    export_file, is_temporary_export = create_excel_export()
    boundary = f'----LeadBot{uuid.uuid4().hex}'

    def field(name, value):
        return (
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
            f'{value}\r\n'
        ).encode('utf-8')

    try:
        document = export_file.read_bytes()
        body = b''.join([
            field('chat_id', chat_id),
            field('caption', 'Royxatdan otgan oquvchilar'),
            (
                f'--{boundary}\r\n'
                'Content-Disposition: form-data; name="document"; filename="Lidlar.xlsx"\r\n'
                'Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\r\n\r\n'
            ).encode('utf-8'),
            document,
            b'\r\n',
            f'--{boundary}--\r\n'.encode('utf-8'),
        ])
        token, _ = load_settings()
        request = Request(
            f'https://api.telegram.org/bot{token}/sendDocument',
            data=body,
            headers={'Content-Type': f'multipart/form-data; boundary={boundary}'},
            method='POST',
        )
        with urlopen(request, timeout=35) as response:
            result = json.loads(response.read().decode('utf-8'))
        if not result.get('ok'):
            raise RuntimeError('Excel file was not sent.')
    finally:
        if is_temporary_export:
            export_file.unlink(missing_ok=True)


def handle_update(update):
    message = update.get('message') or {}
    chat_id = str((message.get('chat') or {}).get('id', ''))
    _, admin_chat_id = load_settings()
    if chat_id != admin_chat_id:
        return

    text = (message.get('text') or '').strip()
    if text.startswith('/start'):
        send_message(chat_id, 'Bot tayyor. Excel faylini olish uchun Excel tugmasini bosing.', True)
    elif text.casefold() in {EXCEL_BUTTON.casefold(), '/excel'}:
        send_excel(chat_id)


def run_bot():
    print('Lead bot started.')
    offset = None
    while True:
        try:
            process_outbox()
            payload = {'timeout': 5, 'allowed_updates': ['message']}
            if offset is not None:
                payload['offset'] = offset
            updates = telegram_request('getUpdates', payload)
            for update in updates:
                offset = update['update_id'] + 1
                handle_update(update)
        except (HTTPError, URLError, TimeoutError, RuntimeError, OSError) as error:
            print(f'Bot error: {error}. Retrying in 5 seconds.')
            time.sleep(5)


if __name__ == '__main__':
    run_bot()
