from django.urls import path, re_path, include
from django.conf.urls import url

from .views import *

app_name = 'cadastro'
urlpatterns = [
    path('', cadastro.as_view(), name='cadastro'),
    path('usuario/',  include([
        re_path('^$', cadastro.renova_senha, name='nova-senha'),
        path('novo/', cadastro.cria_cadastro, name='novo-usuario'),
        path('inscrito/', cadastro.procura_cadastro_por_usuario, name='usuario')
    ]) ),
    path('usuarios/', cadastro.procura_cadastros_por_estado, name='usuarios'),   
]