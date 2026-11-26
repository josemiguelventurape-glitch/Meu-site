from django import forms
from .models import Consoles, Games


class ConsolesForm(forms.ModelForm):
    class Meta:
        model = Consoles
        fields = ['nome']


class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['titulo', 'ano', 'estudio', 'genero', 'status', 'console', 'capa']