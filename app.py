from tabpy.tabpy_server.app.app import TabPyApp
import os

# خواندن پسورد از متغیر محیطی
TABPY_PASSWORD = os.environ.get("TABPY_PASSWORD", "admin:admin")  # مقدار پیشفرض اختیاری

# ایجاد config دینامیکی بدون نیاز به فایل passwords.txt
config = {
    "TabPy": {
        "TABPY_PORT": 9004,
        "TABPY_QUERY_OBJECT_PATH": "./tmp/query_objects",
        "TABPY_STATIC_PATH": "./static",
        # تنظیم مستقیم پسورد در config (بدون فایل)
        "TABPY_PWD_FILE": None,  # غیرفعال کردن فایل پسورد
        "TABPY_PASSWORD": TABPY_PASSWORD  # انتقال پسورد به تنظیمات
    }
}

app = TabPyApp()
application = app._create_wsgi_app()
