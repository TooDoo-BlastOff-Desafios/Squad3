from django.utils.datastructures import MultiValueDictKeyError

def analisarDados(requisicao):
    try:        
        dados = {
            'login': requisicao.POST['login'],
            'senha': requisicao.POST['senha'],
            'nome': requisicao.POST['nome'],
            'cpf': requisicao.POST['cpf'],
            'cidade': requisicao.POST['cidade'],
            'bairro': requisicao.POST['bairro'],
            'rua': requisicao.POST['rua'],
            'numero': requisicao.POST['numero'],
            'complemento': requisicao.POST['complemento'],
            'cep': requisicao.POST['cep'],
        }
        return dados
    except MultiValueDictKeyError:
        return False