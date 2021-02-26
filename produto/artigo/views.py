
from django.db.models.query import QuerySet
from artigo.models import Artigo, Categoria
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.http import HttpResponse as response

from django.views.decorators.http import require_http_methods


# Create your views here.
from .forms import FormularioArtigo

def adiciona_artigo(request, *args):
    if request.POST:

        #foto_data = {'foto': Simple}
        #print(request.POST)
         
        formulario = FormularioArtigo(request.POST, files=request.FILES)

        #print(request.FILES)
        #formulario.clean
        if formulario.is_valid():
            formulario.save(commit=False)
            return redirect('/artigo/mostrar')
        
        else:
            return response('Invalid')
        
    else:
        template_name = "./artigo.html"
        return render(request, template_name,
         {
             'form': FormularioArtigo().as_divs(),
         })

@require_http_methods('POST')
def elimina_artigo(request, id, **kwargs):

    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, pk=id)
        deletions, deleted = artigo.delete(id)

        if deletions >= 1:
            return response("Deleted")
        else:
            return response("Not deleted")
    

    pass

def atualiza_artigo(request, preco, quantidade, unidades):
    pass

def modifica_foto(request):
    pass 

def mostra_artigos(request, *args):
    template_name = './artigos.html'
    categorias = Categoria.objects.all()
    artigos = QuerySet(model=Artigo).all()

    if args is None:
        categorias = Categoria.objects.all()
        artigos = QuerySet(model=Artigo).all()
        return render(request, template_name, {
            'categorias': categorias,
            'artigos': artigos
        })
    if args.__contains__('categoria'):
        return render(request, template_name, {
          'categorias': categorias,
          'artigos': artigos
        })
    else:
        return render(request, template_name, {
        'categorias': categorias,
        'artigos': artigos
        })