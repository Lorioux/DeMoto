from django.db import models

# Create your models here.
'''
Vamos criar um modelo de usuario contendo os campos de referencia basicos de usuario, a saber: o identificador, o email, e palavra-chase encriptada, 
a data de criacao e data de ultima modificacao, estado do registo.
'''
class Usuario (models.Model):
    identificador = models.CharField(max_length=55, blank=False, verbose_name="Utilizador")
    palavra_passe = models.CharField(verbose_name="Palavra-passe", max_length=128, blank=False)
    criado_em = models.DateTimeField(auto_created=True)
    modificado_em = models.DateField(auto_created=False, editable=False)

    ESTADO (
        ('P','PENDENTE'),
        ('I', 'INATIVO'),
        ('A', 'ATIVO')   
    )

    estado = models.CharField(max_length=1, choices=ESTADO, default=ESTADO[0]['P'])

