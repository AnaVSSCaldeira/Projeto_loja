from django.shortcuts import get_object_or_404, render
from projeto.forms import FormProduct, FormSell
from .models import Product, Sell
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.views import View
from django.urls import reverse


class indexView(TemplateView):
    template_name = 'index.html'

class ProductListView(ListView):
    template_name = 'lista_de_produtos.html'
    model = Product
    
class produtos_disponiveis(ListView):
    template_name = 'produtos_ok.html'
    model = Product
    queryset = Product.objects.filter(situacao=True)


class CadastrarProduto(CreateView):
    template_name = 'tela_cadastro.html'
    model = Product
    form_class = FormProduct
    success_url=('/')

class CompraFinalizada(TemplateView):
    template_name = 'compra_finalizada.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        total=self.kwargs.get('total')
        context['total'] = total
        return context

class ComprarProduto(CreateView):
    template_name = 'compra.html'
    model = Sell
    form_class = FormSell
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        product_id=self.kwargs.get('product_id')
        produto = Product.objects.get(pk=product_id)
        context['price'] = produto.price
        context['id_product'] = produto.pk
        return context

    def get_form(self, **kwargs):
        product_id=self.kwargs.get('product_id')
        produto = Product.objects.get(pk=product_id)
        #import pdb; pdb.set_trace()
        form=self.form_class(self.request.POST or None, initial={'id_product':produto})
        return form

    def get_success_url(self):
        context = self.get_context_data()
        quantidade = self.request.POST.get('quantity')
        #import pdb; pdb.set_trace()
        price=float(context['price'])
        quantidade=float(quantidade)
        total = price*quantidade
        return reverse('projeto:compra_finalizada', kwargs={'total':str(total)})

class EditarProduto(UpdateView):
    template_name = 'update_produto.html'
    model = Product
    fields = [
        "name",
        "image",
        "price",
        "stock",
        "situacao"
    ]
    success_url =('/')

'''
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
        form=FormProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
        return redirect(listagem_de_produtos)
    return render(request, 'projeto/tela_cadastro.html',{'form':FormProduct})

def editar_produto(request,id):
    produto=get_object_or_404(Product,pk=id)
    form=FormProduct(request.POST or None, instance=produto)
    if request.POST:
        if form.is_valid():
            form.save() 
        return redirect(listagem_de_produtos)
    return render(request, 'projeto/update_produto.html',{'form':form,'produto':produto})

def comprar_produto(request,id):
    produto=get_object_or_404(Product,pk=id)
    form=FormSell(request.POST or None, initial={'id_product':produto.pk})

    if request.POST:
        if form.is_valid():
            sell=form.save()
            total=sell.quantity*produto.price
            return render(request, 'projeto/compra_finalizada.html',{'total':total})
    return render(request, 'projeto/compra.html',{'form':form,'produto':produto})

'''