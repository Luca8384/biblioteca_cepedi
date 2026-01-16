from django.contrib import admin
from .models import Editora

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome', 'telefone')
    list_filter = ('nome',)
    ordering = ('nome',)
