from django.urls import path

from .views import *

app_name = 'cadastro'
urlpatterns = [
    path('', index, name='cadastro')
]
