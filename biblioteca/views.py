from django.shortcuts import render
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all().order_by('-criado_em')

    context = {
        'livros':livros
    }

    return render(request, 'biblioteca/listar_livros.html', context)