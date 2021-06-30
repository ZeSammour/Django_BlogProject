from django import forms

class cadastrarPublicacao(forms.Form):
    titulo = forms.CharField(max_length=100)
    descricao = forms.CharField(max_length=500)
    nome_autor = forms.CharField(max_length=100)
    sobrenome_autor = forms.CharField(max_length=100)

class filtrarPorAutor(forms.Form):
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
