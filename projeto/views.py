from django.shortcuts import render
from projeto.models import Product

'''produtos=Product.objects.all()
import pdb; pdb.set_trace()'''

def index(request):
    return render(request, 'projeto/index.html', {})

def listagem_de_produtos(request):
    produtos=Product.objects.all()
    return render(request, 'projeto/lista_produtos.html', {'produtos':produtos}) 

def produtos_disponiveis(request):
    produtos=Product.objects.filter(situacao=True)
    return render(request, 'projeto/produtos_ok.html', {'produtos':produtos})