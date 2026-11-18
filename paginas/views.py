from django.shortcuts import render

from django.http import HttpResponse
from .models import Tabela, Category

def Wiki(request):
    dados = {
        "Name":"Mr. Puzzles",
        "City":"The Big Bad's Lair",
        "Age": 21,
        "Height": 1.80,
        "Title": ["TV Boy", "Mr. P", "Boxhead", "TV Guy", "Shakespeare"]
    }
    return render(request, "Wiki.html", dados)

def About(request):
    return render(request, "About.html")

def Contact(request):
    return render(request, "Contact.html")

def Project(request):

    return render(request, "Project.html")

def Project(request):
    projetos = {
         "Projetos": Tabela.objects.all(),
    }
    return render(request, "Project.html", projetos)

def Categories(request):
    Categories = {
         "Categories": Tabela.objects.all(),
    }
    return render(request, "Categories.html", Categories)