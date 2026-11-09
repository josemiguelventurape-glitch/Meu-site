from django.shortcuts import render

from django.http import HttpResponse

def Wiki(request):
    dados = {
        "Name":"Mr. Puzzles",
        "Age": 21,
        "Height": 1.80,
        "Courses": ["Villain","Super Villain","Vilão","SMG4"]
    }
    return render(request, "inicio.html", dados)

def About(request):
    return HttpResponse("<a href='/'>Wiki</a> | "
                        "<a href='/Contact/'>Contato</a> | "
                        "<a href='/About/'>Sobre</a>"
                        "<h1>Sobre Mim</h1>"
                        "<p>teste</p>")

def Contact(request):
    return HttpResponse("<a href='/'>Wiki</a> | "
                        "<a href='/Contact/'>Contato</a> | "
                        "<a href='/About/'>Sobre</a>"
                        "<h1>Contato</h1>"
                        "<p>teste</p>")