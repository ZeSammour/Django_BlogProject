from django import forms

class cadastrarUsuario(forms.Form):
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)