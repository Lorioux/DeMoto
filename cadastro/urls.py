from django.urls import path, re_path, include

from .views import *

app_name = 'cadastro'
urlpatterns = [
    path('', CadastroView.as_view(), name='cadastro'),
    path('usuario/',  include([
        path('senha/', renova_senha, name='nova-senha'),
        path('novo/', cria_cadastro, name='novo-usuario'),
        path('inscrito/', procura_cadastro_por_usuario, name='usuario'),
        path('estado/', modifica_estado_cadastro, name='novo-estado'),
    ]) ),
    path('usuarios/', procura_cadastros_por_estado, name='usuarios'),   
]