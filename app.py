from tabpy.tabpy_server.app.app import TabPyApp
import os

# اضافه کردن لاگ موقت برای بررسی محتویات فایل پسورد
with open('passwords.txt', 'r') as f:
    print("=== Password file contents ===")
    print(f.read())

config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
app = TabPyApp(config_file=config_file)
app.run()
