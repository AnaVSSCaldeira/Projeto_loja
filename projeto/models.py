from datetime import datetime
from email.policy import default
from django.conf import settings
from django.db import models
from django.forms import DateField, EmailField
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=20, help_text='Enter product name')
    image = models.ImageField(blank = True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Sell(models.Model):
    cpf = models.CharField(max_length=14)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=30)
    date =  models.DateField(blank=True, null=True, default=datetime.now())
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name = 'Produto')
    quantity = models.IntegerField()
