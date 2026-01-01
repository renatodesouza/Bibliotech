from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
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

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['nome']

    search_fields = ['nome']

    ordering_fields = ['nome']

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['status', 'autor']

    search_fields = ['titulo', 'autor__nome']

    ordering_fields = ['titulo', 'ano_publicacao']

class ResenhaViewSet(viewsets.ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    # gte (Greater Than or Equal): Maior ou igual a (A partir de...).
    # lte (Less Than or Equal): Menor ou igual a (Até...).
    # year: Filtra apenas pelo ano, ignorando o mês/dia.
    
    filterset_fields = {
        'livro':['exact'],
        'nota':['exact', 'gte', 'lte'],
        'data_resenha':['gte', 'lte', 'year', 'month']
    }


    ordering_fields = ['nota', 'data_resenha']