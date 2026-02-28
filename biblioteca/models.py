from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome
    

class Livro(models.Model):
    STATUS_CHOICES = [
        ('L', 'Lendo'),
        ('F', 'Finalizado'),
        ('P', 'Para Ler')
    ]

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    ano_publicacao = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros')
    arquivo = models.FileField(upload_to='livros/', null=True, blank=True)

    

    def __str__(self):
        return f'{self.titulo} {self.autor.nome}'


class Resenha(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='resenha')
    texto = models.TextField()
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    data_resenha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resenha de {self.livro.titulo} - Nota {self.nota}"
    
