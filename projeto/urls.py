from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_de_produtos', views.listagem_de_produtos, name='lista_de_produtos'),
    path('disponiveis', views.produtos_disponiveis, name='disponiveis'),
    path('cadastrar',views.cadastrar_produto, name='cadastrar'),
    path('editar/<int:id>',views.editar_produto, name='editar'),
    path('comprar/<int:id>',views.comprar_produto, name='comprar'),
]