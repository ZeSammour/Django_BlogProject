from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('AppAutores/', views.autores_page, name='Autores'),
    path('AppAutores/Cadastro/', views.cadastro, name='Cadastro'),
    path('AppAutores/Cadastro/AutorCadastrado/', views.autorCadastrado, name='Cadastro realizado'),
    path('AppAutores/ListaAutores/', views.ListaAutores.as_view(), name='Lista de autores'),
]