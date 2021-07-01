from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import *
from .forms import *

class ListaAutores(ListView):
    model = Autor
    
def cadastro(request):
    form = cadastrarUsuario()
    return render(request, 'AppAutores/cadastro.html',{"form":form})

def autores_page(request):
    return render(request, 'AppAutores/autores_page.html')

def autorCadastrado(request):
    form = cadastrarUsuario(request.POST)
    if form.is_valid():
        n = form.cleaned_data["nome"]
        s = form.cleaned_data["sobrenome"]
        a = Autor(nome=n, sobrenome=s)
        a.save()
    return render(request, 'AppPublicacoes/msg.html', {'msg': 'Autor cadastrado com sucesso!'})


