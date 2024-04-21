from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.IntegerField()
    adres = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Client name - {self.name} \n '
                f' client details - email: {self.email}, telefon: {self.telefon}, adres: {self.adres} \n, '
                f' registered in the store in {self.registration_date}')

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Product name - {self.name} \n '
                f' description product - {self.description} \n, '
                f' price - {self.price}'
                f' registered in the store in {self.added_date}')

class Order(models.Model):
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Client {self.clients} bought {self.products} worth {self.total_amount} '
                f'in {self.order_date}')

