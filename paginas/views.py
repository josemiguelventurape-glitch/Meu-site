from .models import Tabela, Category
from django.shortcuts import render, redirect, get_object_or_404
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
    dados = {
        "Categories": Tabela.objects.select_related("Categoria").order_by("Categoria", "Titulo"),
    }
    return render(request, "Project.html", dados)

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

def Detail_Project(request, id):
    projeto = get_object_or_404(Tabela, id=id)
    if request.method == "POST":
        form = TabelaForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("Categories")
    else:
        form = TabelaForm(instance=projeto)
    return render(request, "Detail_Project.html", {"form": form, "Projects": projeto})

def Edit_Tabela(request, id):
    projeto = get_object_or_404(Tabela, id=id)
    if request.method == "POST":
        form = TabelaForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("Categories")
    else:
        form = TabelaForm(instance=projeto)
    return render(request, "Edit_Tabela.html", {"form": form, "Projects": projeto})

def Delete_Tabela(request, id):
    projeto = get_object_or_404(Tabela, id=id)
    if request.method == "POST":
        projeto.delete()
        return redirect("Categories")
    return render(request, "Delete_Tabela.html", {"Projects": projeto})