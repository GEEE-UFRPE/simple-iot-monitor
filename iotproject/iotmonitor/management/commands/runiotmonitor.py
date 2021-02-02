from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'Run the SimpleIOTMonitor server (iotmonitor app) ' \
           'with the ip provided at ip.txt.'

    def handle(self, *args, **options):
        with open('ip.txt', 'r') as file:
            ip = file.readline()
            management.call_command('runserver', '{}:8000'.format(ip))
