from django.conf import settings
from django.db import models
from django.forms import DateField, EmailField
from django.utils import timezone


class Product(models.Model):
    id = models.Field(primary_key = True)
    name = models.CharField(max_length=20, help_text='Enter product name')
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()
    situacao = models.BooleanField(default=True)

class Sell(models.Model):
    id = models.Field(primary_key = True)
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=30)
    date =  models.DateTimeField(blank=True, null=True)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sell_date(self):
        self.date = timezone.now()
        self.save()