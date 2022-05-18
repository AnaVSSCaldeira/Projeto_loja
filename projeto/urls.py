from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_de_produtos', views.listagem_de_produtos, name='lista_de_produtos'),
    path('disponiveis', views.produtos_disponiveis, name='disponiveis'),
]