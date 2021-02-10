from django.apps import AppConfig
import webbrowser
import os


class IotmonitorConfig(AppConfig):
    name = 'iotmonitor'

    def ready(self):
        # Check if it's running in the startup or not, to prevent running twice on startup and running again on reload
        if os.environ.get('RUN_MAIN') != 'true':
            with open('ip.txt', 'r') as file:
                ip = file.readline()
                webbrowser.open("http://{}:8000/iotmonitor".format(ip))
