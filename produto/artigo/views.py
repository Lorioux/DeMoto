
from django.db.models.query import QuerySet
from artigo.models import Artigo, Categoria
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.http import HttpResponse as response

# Create your views here.
from .forms import FormularioArtigo

def adiciona_artigo(request, *args):
    if request.POST:
    
        formulario = FormularioArtigo()
        formulario.data = request.POST
        formulario.clean
        if formulario.is_valid:
            #formulario.cleaned_data
            formulario.save(commit=False)
            return redirect('/artigo/mostrar')
        #print(data)
        else:
            return response('Invalid')
        #formulario.save(commit=False)
        #return response('Cool')
    else:
        template_name = "./artigo.html"
        return render(request, template_name,
         {
             'form': FormularioArtigo().as_pane(),
         })

def elimina_artigo(request):
    pass

def atualiza_artigo(request, preco, quantidade, unidades):
    pass

def modifica_foto(request):
    pass 

def mostra_artigos(request, *args):
    template_name = './artigos.html'
    if args is None:
        categorias = Categoria.objects.all()
        artigos = QuerySet(model=Artigo).all()
        return render(request, template_name, {
            'categorias': categorias,
            'artigos': artigos
        })
    if args.__contains__('categoria'):
        categorias = Categoria.objects.all()
        artigos = QuerySet(model=Artigo).all()
        return render(request, template_name, {
          'categorias': categorias,
          'artigos': artigos
        })
    else:
        categorias = Categoria.objects.all()
        artigos = Artigo.objects.all()
        return render(request, template_name, {
        'categorias': categorias,
        'artigos': artigos
        })