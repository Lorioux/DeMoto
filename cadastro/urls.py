from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import os

from .views import *

app_name = 'cadastro'
urlpatterns = [
    path('ins/q=', inicio, name='cadastro'),
    path('usuario/',  include([
        path('novo/', cria_cadastro, name='novo-usuario'),
        path('senha/', renova_senha, name='nova-senha'),
        path('estado/', modifica_estado_cadastro, name='novo-estado'),
        path('perfil/', modifica_perfil_cadastro, name='novo-perfil'),
        path('inscrito/', procura_cadastro_por_usuario, name='usuario'),
    ])),
    path('usuarios/', include([
        path('estado/', procura_cadastros_por_estado, name='usuarios-por-estado'),
        path('perfil/', procura_cadastros_por_perfil, name='usuarios-por-perfil'), 
    ])),
] 

urlpatterns += static(
    settings.STATIC_URL, document_root = os.path.join(settings.BASE_DIR, 'cadastro/templates/'),
)