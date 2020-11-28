from django.db.models.query import QuerySet
from django.test import TestCase
from django.db.models import Q
from datetime import datetime

from .models import Cadastro

# Create your tests here.
class CadastroModeloTestCase(TestCase):
    databases = {'cadastros'}
    
    @classmethod
    def setUpTestData(cls):
        cls.modulo = QuerySet(model=Cadastro,  using='cadastros')
        cls.cadastro, cls.criado = cls.modulo.get_or_create(
            usuario='test@test.xyz', 
            palavra_passe='simples', 
            modificado_em=str(datetime.now()), 
            estado = 'PENDENTE',
            chave='xssdedcevevesdvssrvrsvafeagadfdr')
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
                estado = 'ATIVO',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
            Cadastro(
                usuario='test3@gmail.xyz', 
                palavra_passe='simples', 
                modificado_em=str(datetime.now()), 
                estado = 'INATIVO',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
        ]
        
    def test_1_criarcadastro(self):
        """
        Testar a criacao de um cadastro na base dados
        """
        print("Cadastros criados: ", self.criado)
        self.assertTrue(self.criado, msg="Cadastro criado")
        pass

    def test_2_lercadastro(self):
        """
        Testar a leitura do cadastro na base de dados
        """
        self.cadastro = self.modulo.get(usuario='test@test.xyz')
        print("Teste 2: ", self.cadastro)
        self.assertEqual('test@test.xyz', self.cadastro.usuario, msg="Usuario nao encontrado")
        self.assertEqual('PENDENTE', self.cadastro.estado, msg="Estado desconhecido")
        pass

    def test_3_atualizarcadastro(self):
        import datetime
        """
        Testar a atualizacao de um cadastro
        """
        self.modulo.filter(usuario='test@test.xyz').update(estado='INATIVO')
        self.modulo.filter(usuario='test@test.xyz').update(modificado_em =datetime.datetime.now())
        self.cadastro = self.modulo.get(usuario='test@test.xyz')
        print("Teste 3: ", self.cadastro.estado)    
        self.assertEqual('INATIVO', self.cadastro.estado, msg="Estado nao atualizado")
        pass

    def test_4_eliminarcadastro(self):
        """
        Testar a eliminacao de um cadastro na base de dados
        """
        deleted_num, self.cadastro = Cadastro.objects.filter(usuario='test@test.xyz').delete()
        print("Numero de cadastros elinados: ", deleted_num)
        self.assertNotEqual(0, deleted_num, msg="Registo nao eliminado")

    def test_5_criarmultiplocadastros(self):
        """
        Testar a criacao de multiplos cadastros
        """
        count = self.modulo.bulk_create(self.multiplo_cadastros)
        self.assertEqual(3, len(count), msg="Falhou a criacao de multiplo cadastros")

    def test_6_leituramultiplosCadastros(self):
        self.cadastro = self.modulo.values()
        print(self.cadastro)

    def  test_7_eliminarmultiplocadastros(self):
        """
        Testar a elimincao de varios cadastros
        """
        count = Cadastro.objects.filter(Q(estado='INATIVO') & Q(estado='PENDENTE')).delete()
        self.assertEqual(2, len(count), msg="Nada foi eliminado")
        pass


class CadastroApiTestCase(TestCase):

    databases = {'cadastros'}

    def setUp(self):
        super().setUp()
        pass

    def test_criarCadastro(self):
        response = self.client.post('/cadastro/usuario/novo/', data={'usuario':'testapi@test.xyz', 'palavra_passe':'simples'}, extra={'accept':'application/json'})
        #print("Response code: ", response.content)
        self.assertContains(response= response,text='testapi@test.xyz', status_code=200 )
        pass

    def test_leituraCadastro(self):
        response = self.client.get('/cadastro/1/pendente/')
        print("Response code: ", response.content)
        pass

    def test_leituraCadastro(self):
        response = self.client.get('/cadastro/1/pendente/')
        print("Response code: ", response.content)
        pass