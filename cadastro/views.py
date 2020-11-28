from datetime import datetime
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import request, response

from django.views.generic import View, RedirectView

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
            <p>%s</p>
        </body>
        """ % (request.META)

        if request.method == 'GET':
            return response.HttpResponse(content=content)
        
        if request.method == 'POST':
            #criar_cadastro(usuario= kwargs.usuario, palavra_passe=kwargs.palavra_passe)
            return response.HttpResponse(content=content)

    def criar_cadastro(request):
        usuario = request.POST['usuario']
        palavra_passe = request.POST['palavra_passe']
        cadastro = QuerySet(model=Cadastro).create(usuario=usuario, palavra_passe=palavra_passe)
        content = cadastro
        return response.HttpResponse(content=content)

    def procurar_cadastro_por_estado(request, estado):
        cadastros = QuerySet(model=Cadastro).get(estado=estado)
        return response.HttpResponse(content="Achados [ %s ]") % cadastros