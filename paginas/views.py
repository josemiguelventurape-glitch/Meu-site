from django.shortcuts import render

from django.http import HttpResponse

def Wiki(request):
    dados = {
        "Name":"Mr. Puzzles",
        "City":"Villains Planet",
        "Age": 21,
        "Height": 1.80,
        "Title": ["TV Boy", "Mr. P", "Boxhead", "TV Guy", "Shakespeare"]
    }
    return render(request, "Wiki.html", dados)

def About(request):
    return render(request, "About.html")

def Contact(request):
    return render(request, "Contact.html")