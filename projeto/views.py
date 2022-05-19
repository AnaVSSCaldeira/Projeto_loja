import pdb
from django.shortcuts import get_object_or_404, redirect, render
from projeto.forms import NewProduct, NewSell, UpdateProduct
from projeto.models import Product
from projeto.models import Sell

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

def cadastrar_produto(request):
    if request.POST:
        form=NewProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
        return redirect(listagem_de_produtos)
    return render(request, 'projeto/tela_cadastro.html',{'form':NewProduct})


def editar_produto(request,id):
    produto=get_object_or_404(Product,pk=id)
    form=UpdateProduct(request.POST or None, instance=produto)
    if request.POST:
        if form.is_valid():
            form.save() 
        return redirect(listagem_de_produtos)
    return render(request, 'projeto/update_produto.html',{'form':form,'produto':produto})

def comprar_produto(request,id):
    produto=get_object_or_404(Product,pk=id)
    form=NewSell(request.POST or None, initial={'id_product':produto.pk})

    if request.POST:
        if form.is_valid():
            sell=form.save()
            total=sell.quantity*produto.price
            return render(request, 'projeto/compra_finalizada.html',{'total':total})
    return render(request, 'projeto/compra.html',{'form':form,'produto':produto})