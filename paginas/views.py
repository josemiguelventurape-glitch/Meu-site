from django.shortcuts import render, redirect, get_object_or_404
from .models import Consoles, Games
from .forms import ConsolesForm, GamesForm


def Start(request):
    return render(request, "01_Start.html")


def Game(request):
    console_selecionado = request.GET.get("console", "")
    status_selecionado = request.GET.get("status", "")

    # Calcula a ordem de cadastro (por id) separada para zerados e não zerados
    ordem_zerados = {
        jogo_id: idx
        for idx, jogo_id in enumerate(
            Games.objects.filter(status="zerado").order_by("id").values_list("id", flat=True),
            start=1,
        )
    }
    ordem_nao_zerados = {
        jogo_id: idx
        for idx, jogo_id in enumerate(
            Games.objects.filter(status="nao_zerado").order_by("id").values_list("id", flat=True),
            start=1,
        )
    }

    jogos_qs = Games.objects.select_related("console").order_by("-status", "titulo")
    if console_selecionado:
        jogos_qs = jogos_qs.filter(console_id=console_selecionado)
    if status_selecionado:
        jogos_qs = jogos_qs.filter(status=status_selecionado)

    jogos = list(jogos_qs)
    for jogo in jogos:
        if jogo.status == "zerado":
            jogo.ordem_status = ordem_zerados.get(jogo.id)
        else:
            jogo.ordem_status = ordem_nao_zerados.get(jogo.id)

    consoles = Consoles.objects.all().order_by("id")

    dados = {
        "games": jogos,
        "consoles": consoles,
        "console_selecionado": console_selecionado,
        "status_selecionado": status_selecionado,
        "total": len(jogos),
        "total_zerados": sum(1 for j in jogos if j.status == "zerado"),
        "total_nao_zerados": sum(1 for j in jogos if j.status == "nao_zerado"),
    }
    return render(request, "03_Games.html", dados)


def New_Console(request):
    if request.method == "POST":
        form = ConsolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("New_Console")
    else:
        form = ConsolesForm()
    return render(request, "04_New_Console.html", {"form": form})


def New_Game(request):
    if request.method == "POST":
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Games")
    else:
        form = GamesForm()
    return render(request, "05_New_Game.html", {"form": form})


def Detail_Game(request, id):
    game = get_object_or_404(Games, id=id)
    return render(request, "06_Detail_Game.html", {"game": game})


def Edit_Game(request, id):
    game = get_object_or_404(Games, id=id)
    if request.method == "POST":
        form = GamesForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("Games")
    else:
        form = GamesForm(instance=game)
    return render(request, "07_Edit_Game.html", {"form": form, "game": game})


def Delete_Game(request, id):
    game = get_object_or_404(Games, id=id)
    if request.method == "POST":
        game.delete()
        return redirect("Games")
    return render(request, "08_Delete_Game.html", {"game": game})