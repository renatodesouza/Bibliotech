from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from biblioteca.servicies.ai_service import AIService
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

    def get_queryset(self):
        # pega o usuário que está logado
        user = self.request.user

        # Retorna apenas os livros do usuário logado
        return Livro.objects.filter(usuario=user)
    
    # Cria um livro sem pedir o ID do usuário pelo Json
    # o backend vai injetar o usuário logado automatiocamente
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

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


class ChatLivroView(APIView):
    def post(self, request, livro_id):
        pergunta = request.data.get('pergunta')
        
        if not pergunta:
            return Response({"erro": "A pergunta é obrigatória."}, status=400)
            
        try:
            ai = AIService()
            resultado = ai.ask_book(book_id=livro_id, question=pergunta)
            return Response(resultado)
            
        except Exception as e:
            print(f"========== ERRO DA API DO GOOGLE ==========\n{str(e)}\n===========================================")
            # Se for erro de cota (429), enviamos uma mensagem limpa
            if "429" in str(e):
                return Response({
                    "erro": "Limite de requisições atingido. Aguarde 30 segundos e tente novamente."
                }, status=429)
            
            return Response({"erro": str(e)}, status=500)