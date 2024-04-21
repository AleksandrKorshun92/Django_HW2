from django.core.management.base import BaseCommand
from my_program2.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product Name')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('count', type=int, help='Product count')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        price = kwargs.get('price')
        count = kwargs.get('count')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.price = price
        product.count = count
        product.save()
        self.stdout.write(f'{product}')

