from django.urls import path

from .views import *

app_name = 'usuario'
urlpatterns = [
    path('', index, name='usuario')
]
