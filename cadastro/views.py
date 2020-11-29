from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import request, response
import sys

from django.views.generic import RedirectView

from .models import Cadastro

# Create your views here.
class cadastro(RedirectView):

    def get(self, request: request.HttpRequest, *args, **kwargs)-> response.HttpResponse:
        content = """
        <body>
            <p>PEDIDO: %s : %s</p>
        </body>
        """ % (request.path_info, request.GET)
        return response.HttpResponse(content=content)
    
    def post(self, request: request.HttpRequest, *args, **kwargs):
        content = """
        <body>
            <p>ALOCACAO: %s</p>
        </body>
        """ % (request.POST)
        return response.HttpResponse(content=content)

    def index(request):
        content = """
        <body>
            <p> %s </p>
        </body>
        """ % (request.META)

        if request.method == 'GET':
            return response.HttpResponse(content=content)
        
        if request.method == 'POST':
            #criar_cadastro(usuario= kwargs.usuario, palavra_passe=kwargs.palavra_passe)
            return response.HttpResponse(content=content)

    def cria_cadastro(request):
        sys.stdout.write('Test criar cadastros ................\n')
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        cadastro = QuerySet(model=Cadastro).create(usuario=usuario, senha=senha)
        content = cadastro
        return response.HttpResponse(content=content)
    
    def renova_senha(request):
        """Renovacao da senha do usuario
        """
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        cadastro = QuerySet(model=Cadastro).filter(usuario__exact=usuario).update(senha=senha)
        return response.HttpResponse(content=cadastro)
        pass
 
    def procura_cadastro_por_usuario(request):
        #sys.stdout.write(f'Testando procura_cadastro_por_usuario ................{request.GET}\n')
        usuario = request.GET['usuario']
        cadastro = QuerySet(model=Cadastro).get(usuario=usuario)
        return response.HttpResponse(content=cadastro.usuario) #% cadastros.id

    def procura_cadastros_por_estado(request):
        #sys.stdout.write(f'Testa procurando_cadastros_por_estado ................{request.GET}\n')
        estado = request.GET['estado']
        cadastros = QuerySet(model=Cadastro).filter(estado__exact=estado)
        return response.HttpResponse(content=cadastros.count())
    