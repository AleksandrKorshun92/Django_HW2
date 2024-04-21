from django.core.management.base import BaseCommand
from my_program2.models import Client, Product, Order
from .my_generate import genarate_product, generate_price, generate_count

class Command(BaseCommand):
    help = "Create Client"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count new Product')
        help = "Generate fake product"

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(2, count + 1):
            new_client = Client.objects.get(pk=i)
            new_product = Product.objects.get(pk=i)
            new_total = new_product.count * new_product.price
            orders = Order(clients= new_client, total_amount=new_total)
            orders.save()
            orders.products.add(new_product)
            self.stdout.write(f'{orders}')

