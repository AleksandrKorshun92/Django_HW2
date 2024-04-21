from django.core.management.base import BaseCommand
from my_program2.models import Product
from .my_generate import genarate_product, generate_price, generate_count

class Command(BaseCommand):
    help = "Create Client"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count new Product')
        help = "Generate fake product"


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            new_name = genarate_product()
            new_price = generate_price()
            new_count = generate_count()
            description = 'text bla bla'
            products = Product(name=f'{new_name}', description=f'{description*i}', price=new_price,
                            count=new_count)
            products.save()
            self.stdout.write(f'{products}')

