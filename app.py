from tabpy.tabpy_server.app.app import TabPyApp
import os

# خواندن پسورد از متغیر محیطی
tabpy_password = os.environ.get("TABPY_PASSWORD", "admin:admin")

# ساخت فایل موقت در حافظه (بدون نیاز به فایل فیزیکی)
from io import StringIO
password_file = StringIO()
password_file.write(tabpy_password)
password_file.seek(0)

# تنظیم کانفیگ
config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
app = TabPyApp(config_file=config_file)

# بازنویسی متد داخلی برای استفاده از پسورد از متغیر محیطی
app._parse_pwd_file = lambda: password_file

application = app._create_wsgi_app()
