from pathlib import Path
from app.app import app

print(f"Static folder: {app.static_folder}")
print(f"Static URL path: {app.static_url_path}")
print(f"Exists: {Path(app.static_folder).exists()}")
print(f"Files: {list(Path(app.static_folder).glob('*'))[:5]}")
