from typing import Text
from django import forms
from django.db.models.fields import TextField
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms import fields
from django.forms.fields import FileField
from django.forms.models import BaseModelForm, ModelForm
from django.forms.widgets import FileInput, TextInput, Textarea, Widget

from .models import Artigo, Categoria


class FormularioBase(BaseModelForm):
    pass
class FotoInputWidget(forms.FileInput):
    def __init__(self, attrs: dict,) -> None:
        super().__init__(attrs=attrs)

    class Media:
        css = {

        }

class ButtonWidget(forms.widgets.Input):
    input_type = 'submit'
    def __init__(self, attrs: dict,) -> None:
        super().__init__(attrs=attrs)
    pass

class ButtonField(forms.Field):
    widget = ButtonWidget(attrs={'width': '30%', 'height': '10%'})
    pass

class ButtonInput(forms.widgets.Input):
    input_type = 'submit'
    pass

class FormularioArtigo(ModelForm):
    submissao = ButtonField()
    submissao.widget.attrs.update({'style':'width:100px;', 'value':'Adicionar', 'formaction':'/artigo/adicionar', 'formmethod':"POST"})

    class Meta:
        model = Artigo
        fields = ['categoria', 'nome', 'preco', 'moeda', 'quantidade', 'unidade', 'descricao', 'foto']
        widgets = {
            'foto': FileInput(attrs={'width': '30%', 'height': '10%'}),            
        }

    class Media:
        css = {
            'artigo': 'artigo/artigo.css'
        }
    
    def as_pane(self):
        "Return this form rendered as HTML <span>s -- with <br>."
        return self._html_output(
            normal_row='<div%(html_class_attr)s>%(errors)s%(field)s%(help_text)s</div></br>',
            error_row='<span>%s</span>',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    def save(self, commit: bool):    
        if self.errors:
            raise ValueError(
                "Invalid provided data"
        )
        if commit:
            Artigo.objects.update(foto        = self.data['foto'],
                ome        = self.data['nome'],
                reco       = self.data['preco'],
                oeda       = self.data['moeda'],
                uantidade  = self.data['quantidade'],
                nidade     = self.data['unidade'],
                escricao   = self.data['descricao']
                )
        else:
            Artigo.objects.create(categoria_id   = self.data['categoria'] ,
                foto        = self.data['foto'],
                nome        = self.data['nome'],
                preco       = self.data['preco'],
                moeda       = self.data['moeda'],
                quantidade  = self.data['quantidade'],
                unidade     = self.data['unidade'],
                descricao   = self.data['descricao']
                )