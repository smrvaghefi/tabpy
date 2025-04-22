# TabPy Server for Tableau Cloud

این پروژه یک استقرار ساده از [TabPy](https://github.com/tableau/TabPy) است، به صورت امن روی Render.com.

## 🚀 مراحل استقرار

1. این ریپازیتوری را در GitHub ایجاد و فایل‌ها را بارگذاری کن.
2. وارد سایت [Render.com](https://render.com) شو.
3. روی **"New Web Service"** کلیک کن و ریپازیتوری خودت رو انتخاب کن.
4. Render فایل `render.yaml` رو تشخیص می‌ده و خودش تنظیمات رو می‌سازه.
5. بعد از Deploy شدن، آدرس دامنه رو بردار و در **Tableau Cloud > Manage Analytics Extensions** وارد کن.
6. یوزرنیم و پسورد پیش‌فرض: `admin` / `admin`

## ⚙️ تنظیمات امنیتی

برای تغییر یوزرنیم یا پسورد:
- وارد داشبورد سرویس در Render بشو.
- بخش **Environment** رو باز کن.
- مقدار متغیر `TABPY_PASSWORD_ENTRY` رو تغییر بده (مثل `user123:securePassword`).

