from django import forms
from django.forms import HiddenInput, ModelForm
from .models import Product
from .models import Sell

class FormProduct(forms.ModelForm):#FormProduct
    name = forms.CharField(max_length=20)
    image = forms.ImageField(required=False)
    price = forms.DecimalField(decimal_places=2, max_digits=10, initial=0)
    stock = forms.IntegerField()
    situacao = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ['name','image','price','stock','situacao']


class FormSell(forms.ModelForm):
    cpf = forms.CharField(max_length=14)
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(max_length=30)
    date = forms.DateField(widget = forms.SelectDateWidget)
    id_product=forms.ModelChoiceField(queryset=Product.objects.all(), widget = HiddenInput())
    quantity = forms.IntegerField()

    class Meta:
        model = Sell
        fields = ['cpf','name','email','address','date','id_product','quantity']
        
