from tabpy.tabpy_server.app.app import TabPyApp
import os
from pathlib import Path

# خواندن پسورد از متغیر محیطی
TABPY_AUTH = os.environ.get("TABPY_AUTH", "admin:SecurePass123!")

# ایجاد فایل passwords.txt با فرمت صحیح
passwords_content = f"""[users]
{TABPY_AUTH.split(':')[0]} = {TABPY_AUTH.split(':')[1]}

[roles]
{TABPY_AUTH.split(':')[0]} = admin
"""

# ذخیره فایل
passwords_path = Path(__file__).parent / "passwords.txt"
passwords_path.write_text(passwords_content)

# اجرای برنامه
app = TabPyApp(config_file=os.path.join(os.path.dirname(__file__), 'tabpy.conf'))
application = app._create_wsgi_app()
