from email.policy import default
from django import forms
from django.forms import ModelForm
from pkg_resources import require
from .models import Product

class NewProduct(ModelForm):
    name = forms.CharField(max_length=20, help_text='Enter product name')
    image = forms.ImageField(required=False)
    price = forms.DecimalField(decimal_places=2, max_digits=10, initial=0)
    stock = forms.IntegerField()
    situacao = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ['name','image','price','stock','situacao']

class UpdateProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','price','stock','situacao']

class Sell(forms.ModelForm):
    cpf = forms.CharField(max_length=14)
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=254)
    adress = forms.CharField(max_length=30)
    date = forms.DateField(widget = forms.SelectDateWidget)
    quantity = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['cpf','name','email','adress','date','quantity']
        
