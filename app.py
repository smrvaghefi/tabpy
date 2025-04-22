from tabpy.tabpy_server.app.app import TabPyApp
import os

class AuthManager:
    def __init__(self):
        self.username = os.environ["TABPY_USERNAME"]
        self.password = os.environ["TABPY_PASSWORD"]
    
    def authenticate(self, user, pwd):
        return user == self.username and pwd == self.password

# تنظیمات را مستقیماً در کد تعریف می‌کنیم
config = {
    "TabPy": {
        "TABPY_PORT": os.getenv("PORT", "9004"),
        "TABPY_QUERY_OBJECT_PATH": "./tmp/query_objects",
        "TABPY_STATIC_PATH": "./static",
        "TABPY_PWD_FILE": None  # غیرفعال کردن فایل پسورد
    }
}

# ایجاد نمونه برنامه
app = TabPyApp(config_dict=config)

# تنظیم احراز هویت سفارشی
auth = AuthManager()
app._TabPyApp__check_credentials = lambda u, p: auth.authenticate(u, p)

# در TabPy 2.13.0، خود app یک WSGI application است
application = app
