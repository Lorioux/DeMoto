from django.urls import path, re_path, include
from django.conf.urls import url

from .views import *

app_name = 'cadastro'
urlpatterns = [
    path('', cadastro.as_view(), name='cadastro'),
    path('usuario/novo/', cadastro.criar_cadastro, name='novo-cadastro'),
    path('usuario/<str:id>/', cadastro.procurar_cadastro_por_id),
    path('usuario/<str:estado>/', cadastro.procurar_cadastros_por_estado)
    
]
