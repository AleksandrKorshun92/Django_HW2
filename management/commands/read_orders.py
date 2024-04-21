from django.core.management.base import BaseCommand
from my_program2.models import Order


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk)
        self.stdout.write(f'{order}')