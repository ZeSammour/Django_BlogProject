from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.db.models import Q

from .models import *
from .forms import *
from AppAutores.models import *

class ListaPublicacoes(ListView):
    model = Publicacao

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = filtrarPorAutor()
        return context

# Create your views here.
def publicacoes_page(request):
    return render(request, 'AppPublicacoes/publicacoes_page.html')

def cadastro(request):
    form = cadastrarPublicacao()
    return render(request, 'AppPublicacoes/cadastro.html',{"form":form})

def publicacaoCadastrada(request):
    form = cadastrarPublicacao(request.POST)
    if form.is_valid():
        t = form.cleaned_data["titulo"]
        d = form.cleaned_data["descricao"]
        n = form.cleaned_data["nome_autor"]
        s = form.cleaned_data["sobrenome_autor"]
        try:
            a = Autor.objects.get(nome=n, sobrenome=s)
            p = Publicacao(titulo=t, descricao=d, autor=a)
            p.save()
            return HttpResponse('<h1>Publicação Cadastrada</h1>')
        except:
            return HttpResponse('<h1>Autor(a) não cadastrado(a)</h1>')    

def publicacoesPorAutor(request):
    form = filtrarPorAutor(request.POST)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sobrenome = form.cleaned_data["sobrenome"]
        try:
            a = Autor.objects.get(nome=nome, sobrenome=sobrenome)
            publicacoes_autor = a.publicacao_set.all()
            numero_publicacoes = a.publicacao_set.count()
            return render(request, 'AppPublicacoes/filtro_list.html',{"publicacoes":publicacoes_autor, "numero_publicacoes":numero_publicacoes, "autor":a,})
        except:
            return HttpResponse('<h1>  Autor não encontrado</h1>')
    



