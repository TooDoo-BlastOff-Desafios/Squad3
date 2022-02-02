from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Notificacao
from .complementos.serializers import usuarioRelacionado
from .complementos.cadastros.cadastrarUsuarios import Cadastro
from .complementos.cadastros.verificaDadosRequisicao import analisarDados

class mostrarUsuarios(generics.ListAPIView):
    serializer_class = usuarioRelacionado.userSerializer

    def get_queryset(self): 
        query_set = User.objects.filter(username=self.request.user)       
        

        return query_set

class mostrarNotificacao(generics.ListAPIView):
    serializer_class = usuarioRelacionado.notificacaoSerializer

    def get_queryset(self):
        query_set = Notificacao.objects.filter(usuario=self.request.user)
        
        return query_set

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def cadastrarUsuario(request):
    dadosAnalisados = analisarDados(request)
    if dadosAnalisados == False:        
        return Response('Envie informacões corretas')
    
    cadastro = Cadastro()
    
    cadastro.cadastroLogin(dadosAnalisados['login'], dadosAnalisados['senha'])
    cadastro.cadastroUsuario(dadosAnalisados['nome'], dadosAnalisados['cpf'])
    cadastro.cadastroEndereco(dadosAnalisados['cidade'], dadosAnalisados['bairro'],
                    dadosAnalisados['bairro'], dadosAnalisados['rua'],
                    dadosAnalisados['numero'], dadosAnalisados['complemento'],
                    dadosAnalisados['cep'])
    
    return Response('Login salvo com sucesso')
