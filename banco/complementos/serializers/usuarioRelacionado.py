from rest_framework import serializers
from banco.models import Usuario, Endereco, Notificacao
from django.contrib.auth.models import User

class notificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = ['mensagem', 'data']


class enderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep', 'cidade', 'bairro', 'rua', 'numero', 'complemento']


class usuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['numeroConta', 'nome', 'cpf']

class userSerializer(serializers.ModelSerializer):
    enderecos = enderecoSerializer(many=True, read_only=True)
    notificacoes = notificacaoSerializer(many=True, read_only=True)
    usuarios = usuarioSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'usuarios', 'enderecos', 'notificacoes']