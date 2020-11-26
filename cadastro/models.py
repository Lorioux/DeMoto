from django.db import models
from django.db.models import fields
from django.db.models.constraints import UniqueConstraint
from django.db.models.expressions import OrderBy
from django.db.models.lookups import Regex
import datetime

# Create your models here.

class Cadastro(models.Model):
    """
    Vamos criar um modelo de usuario contendo os campos de referencia basicos de usuario, a saber: o identificador, o email, e palavra-chase encriptada, 
    a data de criacao e data de ultima modificacao, estado do registo.
    """
    usuario = models.CharField(verbose_name="Utilizador", 
        max_length=55, 
        blank=False, 
        primary_key=True,
        unique=True)
    palavra_passe = models.CharField(verbose_name="Palavra-passe", max_length=128, blank=False)
    criado_em = models.DateTimeField(auto_created=True, default=str(datetime.datetime.now()))
    modificado_em = models.DateTimeField(auto_created=False, editable=False)

    ESTADO = (
        ('P','PENDENTE'),
        ('I', 'INATIVO'),
        ('A', 'ATIVO')   
    )

    estado = models.CharField(max_length=1, choices=ESTADO, default="PENDENTE")
    chave = models.CharField(max_length=255, blank=False, editable=False)

    class Meta:
        ordering = ['usuario', 'palavra_passe']
        UniqueConstraint(
            fields = ['usuario'],
            name = 'usuario_unico'
        )

    def __str__(self):
        return self.usuario

    def eliminar_cadastro(self, usuario=None):
        return self.objects.filter(usuario=usuario).delete()

