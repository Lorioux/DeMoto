from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', VistaProduto.as_view(), name='inicio'),
    path('produto/?(?p<nome>[a-zA-Z].+)', VistaProduto.put, name='novo-produto')
]