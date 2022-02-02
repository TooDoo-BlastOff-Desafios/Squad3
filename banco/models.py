from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    numeroConta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    login = models.ForeignKey(User, related_name='usuarios', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nome)

class Endereco(models.Model):
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.TextField()
    cep = models.CharField(max_length=9)
    usuario = models.ForeignKey(User, related_name='enderecos', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.cidade)

class Transferencia(models.Model):
    remetente = models.ForeignKey(User, related_name='transferencias', on_delete=models.CASCADE)
    comentario = models.TextField()
    destinatario = models.IntegerField()
    dataTransferencia = models.DateTimeField(auto_now_add=True) 

class Notificacao(models.Model):
    data = models.DateField(auto_now_add=True)
    mensagem = models.TextField()
    usuario = models.ForeignKey(User, related_name='notificacoes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data)
