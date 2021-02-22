from django.forms import ModelForm, models

from .models import Artigo

class FormularioArtigo(ModelForm):
    class Meta:
        model = Artigo
        fields = ['categoria', 'foto', 'nome', 'preco', 'moeda', 'quantidade', 'unidade', 'descricao']
