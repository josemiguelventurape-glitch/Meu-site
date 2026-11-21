from .models import Tabela, Category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from paginas.forms import TabelaForm, CategoryForm


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
    dados = {
        "Categories": Tabela.objects.select_related("Categoria").order_by("Categoria", "Titulo"),
    }
    return render(request, "Categories.html", dados)

def New_Tabela(request):
    if request.method == "POST":
        form = TabelaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/New_Tabela/")
    else:
        form = TabelaForm()
    return render(request, "New_Tabela.html",
                  {"form": form})

def New_Categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/New_Categories/")
    else:
        form = CategoryForm()
    return render(request, "New_Categories.html",
                  {"form": form})
