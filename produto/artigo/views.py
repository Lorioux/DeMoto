from django.shortcuts import render
from django.views.generic import RedirectView

# Create your views here.
from .models import FormularioProduto
class VistaProduto(RedirectView):

    def get(self, request, *args, **kwargs):
        template_name = 'inicio.html'
        formulario = FormularioProduto()
        return render(request, template_name, {
            'form': formulario
        })
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def head(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

