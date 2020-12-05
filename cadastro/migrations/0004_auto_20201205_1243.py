# Generated by Django 3.1.4 on 2020-12-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20201129_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='perfil',
            field=models.CharField(choices=[('FO', 'FORNECEDOR'), ('CO', 'CONSUMIDOR'), ('AG', 'AGENTE'), ('CD', 'CONDUTOR')], default='CONSUMIDOR', max_length=2, verbose_name='Perfil do usuario'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='criado_em',
            field=models.DateTimeField(auto_created=True, default='2020-12-05 12:43:44.219021'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='estado',
            field=models.CharField(choices=[('P', 'PENDENTE'), ('I', 'INATIVO'), ('A', 'ATIVO'), ('S', 'SUSPENSO')], default='PENDENTE', max_length=1),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='modificado_em',
            field=models.DateTimeField(default='2020-12-05 12:43:44.219091', editable=False),
        ),
    ]
