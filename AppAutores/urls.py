from django.urls import path

from . import views

urlpatterns = [
    path('', views.autores_page, name='Autores'),
    path('Cadastro/', views.cadastro, name='Cadastro Autor'),
    path('Cadastro/AutorCadastrado/', views.autorCadastrado, name='Cadastro realizado'),
    path('ListaAutores/', views.ListaAutores.as_view(), name='Lista de autores'),
]