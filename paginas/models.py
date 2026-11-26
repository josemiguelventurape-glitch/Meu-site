from django.db import models


class Consoles(models.Model):
    nome = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.nome


class Games(models.Model):
    STATUS_CHOICES = [
        ("zerado", "Zerado"),
        ("nao_zerado", "Não zerado"),
    ]

    titulo = models.CharField("Título", max_length=100)
    ano = models.IntegerField("Ano")
    estudio = models.CharField("Estúdio", max_length=100)
    genero = models.CharField("Gênero", max_length=100)
    status = models.CharField(
        "Status",
        max_length=20,
        choices=STATUS_CHOICES,
        default="nao_zerado",
    )
    capa = models.URLField("Link da capa", max_length=500, blank=True)
    console = models.ForeignKey(
        Consoles,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Console",
    )

    def __str__(self):
        return self.titulo