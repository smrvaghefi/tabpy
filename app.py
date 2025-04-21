from tabpy.tabpy_server.app.app import TabPyApp
import os

config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
app = TabPyApp(config_file=config_file)
app.run()
