from django.urls import path
from . import views
#from .views import ProductListView

app_name = 'projeto'

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('lista_de_produtos/', views.ProductListView.as_view(), name='lista_de_produtos'),
    path('disponiveis', views.produtos_disponiveis.as_view(), name='disponiveis'),
    path('cadastrar/',views.CadastrarProduto.as_view(), name='cadastrar'),
    path('editar/<slug:pk>/',views.EditarProduto.as_view(), name='editar'),
    path('comprar/<int:product_id>/',views.ComprarProduto.as_view(), name='comprar'),
    path('compra_finalizada/<str:total>/',views.CompraFinalizada.as_view(), name='compra_finalizada'),
]

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('lista_de_produtos', views.listagem_de_produtos, name='lista_de_produtos'),
    path('disponiveis', views.produtos_disponiveis, name='disponiveis'),
    path('cadastrar',views.cadastrar_produto, name='cadastrar'),
    path('editar/<int:id>',views.editar_produto, name='editar'),
    path('comprar/<int:id>',views.comprar_produto, name='comprar'),
]
'''