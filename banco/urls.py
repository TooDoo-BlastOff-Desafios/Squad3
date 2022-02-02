from django.urls import path

from .views import mostrarUsuarios, mostrarNotificacao, cadastrarUsuario

urlpatterns = [
    path('usuarios/', mostrarUsuarios.as_view(), name='usuarios'),
    #path('notificacoes/', mostrarNotificacao.as_view(), name='notificacoes'),
    path('cadastrarUsuario/', cadastrarUsuario, name='teste')
]