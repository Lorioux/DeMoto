"""microservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from produto.artigo.views import formulario
from artigo.views import (
    adiciona_artigo,
    elimina_artigo,
    mostra_artigos
)
from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

 

urlpatterns = [
    re_path('^artigo/adicionar$', adiciona_artigo, name='adiciona-artigo'),
    re_path('^artigo/mostrar?$', mostra_artigos, name='mostra-artigos'),
    re_path('^artigo/eliminar/(?P<id>.)$', elimina_artigo, name='elimina-artigo')
]

urlpatterns += [
    re_path('^admin/', admin.site.urls),
]
urlpatterns += static(
    settings.STATIC_URL, document_root =  settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
)

