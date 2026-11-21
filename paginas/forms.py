from django import forms
from .models import Tabela,Category

class TabelaForm(forms.ModelForm):
    class Meta:
        model = Tabela
        fields = ['Titulo', 'Ano', 'Estudio', 'IMDb', 'Genero', 'Categoria']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nome']