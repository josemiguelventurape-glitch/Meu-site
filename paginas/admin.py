from django.contrib import admin
from .models import Consoles, Games


@admin.register(Consoles)
class ConsolesAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano', 'estudio', 'genero', 'console']
    list_filter = ['console', 'genero']
    search_fields = ['titulo', 'estudio']