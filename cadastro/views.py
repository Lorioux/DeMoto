from datetime import datetime
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
import sys

from django.views.generic import RedirectView
from django.views.decorators.http import require_http_methods

from .models import Cadastro

# Create your views here.
class CadastroView(RedirectView):

    def get(self, request, *args, **kwargs)-> HttpResponse:
        pass
    
    def post(self, request, *args, **kwargs):
        pass

    def index(request):
       pass

def cria_cadastro(request):
    """Criacao de novo cadastro com base nos valores de  [usuario e senha] fornecidos no request.
    Args:
        request: HttpRequest, com o metodo POST
    Retorna:
        repos

    """
    #sys.stdout.write('Test criar cadastros ................\n')
    usuario = request.POST['usuario']
    senha = request.POST['senha']
    cadastro = QuerySet(model=Cadastro).create(usuario=usuario, senha=senha)
    return HttpResponse(content=cadastro)

def renova_senha(request):
    """Renovacao da senha do usuario no cadastro. A partir do [usuario] fornecido verifica-se a existencia de um 
    registo nos cadastos e procede-se a substituicao da senha atual, com o valor da [senha] fornecida no request.

    Args:
        request: HttpRequest, com o metodo POST
    Retorna:
        response: HttpResponse, a resposta com o numero de registos com usuario especfico fora atualizadas senha. 
    """
    usuario = request.POST['usuario']
    senha = request.POST['senha']
    numero_de_registos_atualizados = QuerySet(model=Cadastro).filter(usuario__exact=usuario).update(senha=senha)
    return HttpResponse(content=numero_de_registos_atualizados)

@require_http_methods(['POST'])
def modifica_estado_cadastro(request):
    """Modificao do estado do cadastro com base no [usuario] indicado no request. Achar o registo e altera o [estado] para
    o valor indicado pelo [estado] no request:

    Args:
        requst: HttpRequest, com o metodo PUT

    Retorna:
        response: HttpRespose, contendo o numero de registos actualizados
    """
    data =  request.POST
    #sys.stdout.writelines(('Testando ---modificacao do estado.\n', request))
    usuario = data['usuario']
    estado  = data['estado']
    numero_de_modificacoes = QuerySet(model=Cadastro).filter(usuario=usuario).update(estado=estado, modificado_em=datetime.now())
    return HttpResponse(content=numero_de_modificacoes)

def procura_cadastro_por_usuario(request):
    """Pesquisa de cadastros atraves do usuario provido no pedido. procurar na base de dados de cadastros o registo 
    com o [usuario] fornecido.

    Args:
        request: HttpRequest, com metodo GET
    Retorna:
        response: HttpResponse, contem o objecto cadasto se existe um registo com o usuario ou nulo se nao existe.
    """
    #sys.stdout.write(f'Testando procura_cadastro_por_usuario ................{request.GET}\n')
    usuario = request.GET['usuario']
    cadastro = QuerySet(model=Cadastro).get(usuario=usuario)
    return HttpResponse(content=cadastro.usuario)

def procura_cadastros_por_estado(request):
    """Pesquisa de cadasto que tenha o [estado] fornecido no request a partir do [usuario] indicado.

    Args:
        request: HttpRequest, com o metodo GET
    Retorna:
        reponse: HttpRespose, contendo o [numero_de_registos] encontrados no cadasto.
    """
    #sys.stdout.write(f'Testa procurando_cadastros_por_estado ................{request.GET}\n')
    estado = request.GET['estado']
    numero_de_registos = QuerySet(model=Cadastro).filter(estado__exact=estado).count()
    return HttpResponse(content=numero_de_registos)
