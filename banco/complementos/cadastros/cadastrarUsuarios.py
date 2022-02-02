from django.contrib.auth.models import User

from banco.models import Endereco, Usuario
class Cadastro():    

    def cadastroLogin(self, *dadosLogin):
        login = User(
            username = dadosLogin[0]            
        )
        login.set_password(dadosLogin[1])
        login.save()

        self.login = User.objects.get(username=dadosLogin[0])

    def cadastroUsuario(self, *dadosUsuario):
        usuario = Usuario(
            nome = dadosUsuario[0],
            cpf = dadosUsuario[1],
            login = self.login
        )
        usuario.save()

    def cadastroEndereco(self, *dadosEndereco):
        endereco = Endereco(
            cidade = dadosEndereco[0],
            bairro = dadosEndereco[1],
            rua = dadosEndereco[2],
            numero = dadosEndereco[3],
            complemento = dadosEndereco[4],
            cep = dadosEndereco[5],
            usuario = self.login         
        )
        endereco.save()