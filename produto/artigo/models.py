from django.db import models
from django.forms import ModelForm

# Create your models here.
MOEDA = [
            ('EUR', 'Euro'),
            ('USD', 'Dollar'),
            ('MZN', 'Metical'),
            ('ZAR', 'Rand')
        ]

UNIDADE = [
            ('gr', 'Gramas'),
            ('kg', 'Quilogramas'),
            ('fa', 'Fatias'),
            ('lt', 'Litros'),
        ]

class Artigo(models.Model):
    referencia  = models.CharField('Referencia', blank=True, default='Ref_00', max_length=55)
    categoria   = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING,to_field='designacao', max_length=55)
    foto        = models.ImageField('Imagem', blank=False, default=None, width_field='', height_field='')
    nome        = models.CharField('Produto', blank=False, default='Sumo', max_length=55)
    preco       = models.FloatField('Preço', blank=False, default='0.00', max_length=55)
    moeda       = models.CharField('Moeda', choices=MOEDA, default='EUR', max_length=3)
    quantidade  = models.FloatField('Quantidade', blank=False, default='1.0', max_length=55)
    unidade     = models.CharField('Unidades', choices=UNIDADE, default='kg', max_length=2)
    descricao   = models.TextField('Descrição', blank=False, default='Simples descrição do produto', max_length=256)


    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

class Categoria(models.Model):
    designacao  = models.CharField('Designação', blank=False, default='', unique=True, max_length=55)

    def __repr__(self):
        return self.designacao

    def __str__(self) -> str:
        return self.designacao




