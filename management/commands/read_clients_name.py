from django.core.management.base import BaseCommand
from my_program2.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client Name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        client = Client.objects.filter(name=name)
        self.stdout.write(f'{client}')

