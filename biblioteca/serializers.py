from rest_framework import serializers
from django.db.models import Avg
from .models import Autor, Livro, Resenha


class AutorSerializer(serializers.ModelSerializer):

    total_livros = serializers.SerializerMethodField()
    class Meta:
        model = Autor
        fields = '__all__'

    def get_total_livros(self, obj):
        # obj.livros vem do related_name='livros'
        return obj.livros.count()

class LivroSerializer(serializers.ModelSerializer):
    # Isso mostra o nome do autor em vez de apenas o ID
    autor_nome = serializers.ReadOnlyField(source='autor.nome')

    media_notas = serializers.SerializerMethodField()

    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Livro
        fields = '__all__'

    def get_media_notas(self, obj):
        media = obj.resenha.aggregate(Avg('nota'))['nota__avg']

        return round(media, 1) if media else 0

class ResenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resenha
        fields = '__all__'