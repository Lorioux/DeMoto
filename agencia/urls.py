
from django.urls import path

from .views import *

app_name = 'agencia'
urlpatterns = [
    path('', home, name='in')
]

