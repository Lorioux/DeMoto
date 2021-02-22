from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Categoria)
class AdminCategorias(admin.ModelAdmin):
    list_display = ['designacao']
    fields = ['designacao']
    pass

@admin.register(Artigo)
class AdminProdutos(admin.ModelAdmin):
    list_display = ['nome','preco', 'moeda', 'quantidade', 'unidade']
