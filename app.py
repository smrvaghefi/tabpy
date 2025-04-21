from tabpy.tabpy_server.app.app import TabPyApp
import os
from pathlib import Path

# خواندن پسورد از متغیر محیطی
TABPY_PASSWORD = os.environ.get("TABPY_PASSWORD", "admin:ComplexPass123!")

# ایجاد فایل موقت passwords.txt در مسیر مورد نیاز
passwords_path = Path(__file__).parent / "passwords.txt"
passwords_path.write_text(TABPY_PASSWORD)

# تنظیمات اصلی
config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
app = TabPyApp(config_file=config_file)
application = app._create_wsgi_app()
