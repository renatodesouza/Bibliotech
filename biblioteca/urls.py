from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# Cria o router e registra as novas viewsets
router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'livros', views.LivroViewSet)
router.register(r'resenha', views.ResenhaViewSet)


urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('livros/<int:livro_id>/chat/', views.ChatLivroView.as_view(), name='chat-livro'),
    path('api/', include(router.urls)),
]