@echo off
cd /d "%~dp0"

start "Lead bot" /b ".venv-1\Scripts\python.exe" "Leed bot\bot.py"

".venv-1\Scripts\python.exe" "app\app.py"

pause
