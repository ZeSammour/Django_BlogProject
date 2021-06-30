from django.urls import path

from . import views

urlpatterns = [
    path('', views.publicacoes_page, name='Publicacoes'),
    path('Cadastro/', views.cadastro, name='Cadastro'),
    path('Cadastro/PublicacaoCadastrada/', views.publicacaoCadastrada, name='PublicacaoCadastrada'),
    path('ListaPublicacoes/', views.ListaPublicacoes.as_view(), name='Lista de publicacoes'),
    path('ListaPublicacoes/Filtro/', views.publicacoesPorAutor, name='Filtro por Autor'),
]