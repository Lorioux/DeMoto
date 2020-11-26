from django.test import TestCase
from datetime import datetime
from django.utils.translation import gettext_lazy

from .models import Cadastro

# Create your tests here.
class CadastroTestCase(TestCase):
    databases = {'cadastros'}
    
    @classmethod
    def setUpTestData(cls):
        cls.cadastro, cls.criado = Cadastro.objects.get_or_create(
            usuario='test@test.xyz', 
            palavra_passe='simples', 
            modificado_em=str(datetime.now()), 
            estado = 'PENDENTE',
            chave='xssdedcevevesdvssrvrsvafeagadfdr' )

        cls.multiplo_cadastros = [
            Cadastro(
                usuario='ana@email.xyz', 
                palavra_passe='simples', 
                modificado_em=str(datetime.now()), 
                estado = 'PENDENTE',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
            Cadastro(
                usuario='magido@gmail.xyz', 
                palavra_passe='simples', 
                modificado_em=str(datetime.now()), 
                estado = 'PENDENTE',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
        ]
        
    def test_1_criarcadastro(self):
        """
        Testar a criacao de um cadastro na base dados
        """
        print("Cadastros criados: ", self.cadastro)
        self.assertTrue(self.criado, msg="Cadastro criado")
        pass

    def test_2_lercadastro(self):
        """
        Testar a leitura do cadastro na base de dados
        """
        self.assertEqual('test@test.xyz', self.cadastro.usuario, msg="Email nao encontrado")
        self.assertEqual('PENDENTE', self.cadastro.estado, msg="Estado desconhecido")
        pass

    def test_3_atualizarcadastro(self):
        """
        Testar a atualizacao de um cadastro
        """
        setattr(self.cadastro, 'estado', 'INATIVO')
        self.assertEqual('INATIVO', self.cadastro.estado, msg="Estado nao atualizado")
        pass

    def test_4_eliminarcadastro(self):
        """
        Testar a eliminacao de um cadastro na base de dados
        """
        count = Cadastro.objects.filter(usuario='test@test.xyz').delete()
        print("Numero de cadastros elinados: ", count)
        self.assertNotEqual(0, count, msg="Registo nao eliminado")

    def test_5_criarmultiplocadastros(self):
        """
        Testar a criacao de multiplos cadastros
        """
        count = Cadastro.objects.bulk_create(self.multiplo_cadastros)
        self.assertEqual(2, len(count), msg="Falhou a criacao de multiplo cadastros")