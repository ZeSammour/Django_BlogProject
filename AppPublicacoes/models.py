from django.db import models

from AppAutores.models import Autor

# Create your models here.
class Publicacao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return (self.titulo)
