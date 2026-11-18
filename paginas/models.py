from django.db import models

class Category(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Tabela(models.Model):
    Titulo = models.CharField(max_length=100)
    Ano = models.IntegerField()
    Estudio = models.CharField(max_length=100)
    IMDb = models.FloatField(max_length=100)
    Genero = models.TextField(max_length=1000)
    Categoria = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )