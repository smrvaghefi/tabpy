from tabpy.tabpy_server.app.app import TabPyApp
import os

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
app_instance = TabPyApp(config_file=config_file)
app = app_instance._create_wsgi_app()
