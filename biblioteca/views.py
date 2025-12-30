from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Livro, Autor, Resenha
from .serializers import AutorSerializer, LivroSerializer, ResenhaSerializer

def listar_livros(request):
    livros = Livro.objects.all().order_by('-criado_em')

    context = {
        'livros':livros
    }

    return render(request, 'biblioteca/listar_livros.html', context)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['status', 'autor']

    search_fields = ['titulo', 'autor__nome']

    ordering_fields = ['titulo', 'ano_publicacao']

class ResenhaViewSet(viewsets.ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer