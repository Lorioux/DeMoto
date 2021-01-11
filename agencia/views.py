from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def inicio (request):
    """
    Render a simple html document as home page
    """
    template_name = "agencia/inicio.html"
    
    return  render(request, template_name, {'site_title':"DEMOTO"})
    #return render(request, template_name)
