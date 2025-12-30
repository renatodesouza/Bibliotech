from rest_framework import serializers
from .models import Autor, Livro, Resenha


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    # Isso mostra o nome do autor em vez de apenas o ID
    autor_nome = serializers.ReadOnlyField(source='autor.nome')
    class Meta:
        model = Livro
        fields = '__all__'

class ResenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resenha
        fields = '__all__'