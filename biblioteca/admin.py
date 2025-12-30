from django.contrib import admin
from .models import Autor, Livro, Resenha


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'status', 'ano_publicacao')
    list_filter = ('status', 'autor')
    search_fields = ('titulo', 'autor__nome')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'biografia')

    search_fields = ('nome',)

    fieldsets = [
        ('Nome',        {'fields':('nome',)}),
        ('Biografia',   {'fields':('biografia',)})
    ]

@admin.register(Resenha)
class ResenhaAdmin(admin.ModelAdmin):
    list_display = ('livro', 'texto', 'nota', 'data_resenha')

    search_fields = ('livro', 'data_resenha')

    fieldsets = [
        ('Livro',       {'fields':('livros', 'nota')}),
        ('Texto',       {'fields':('texto',)}),
        ('Data',        {'fields':('data_resenha',)})
    ]
