from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = '''
        <body>
            <p>Teste de usuario</p>
        </body>
        '''
    return render(request, template_name)