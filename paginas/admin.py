from django.contrib import admin

from .models import Tabela, Category


class TabelaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Ano', 'Estudio', 'IMDb', 'Genero', 'Categoria')


admin.site.register(Category)
admin.site.register(Tabela, TabelaAdmin)

