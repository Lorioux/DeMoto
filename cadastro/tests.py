from django.db.models.query import QuerySet
from django.http import response
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
            senha='simples', 
            modificado_em=str(datetime.now()), 
            estado = 'PENDENTE',
            chave='xssdedcevevesdvssrvrsvafeagadfdr')
        cls.multiplo_cadastros = [
            Cadastro(
                usuario='ana@email.xyz', 
                senha='simples', 
                modificado_em=str(datetime.now()), 
                estado = 'PENDENTE',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
            Cadastro(
                usuario='magido@gmail.xyz', 
                senha='simples', 
                modificado_em=str(datetime.now()), 
                estado = 'ATIVO',
                chave='xssdedcevevesdvssrvrsvafeagadfdr'
            ),
            Cadastro(
                usuario='test3@gmail.xyz', 
                senha='simples', 
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

    def test_1_cria_novo_cadastro(self):
        response = self.client.post('/cadastro/usuario/novo/', data={'usuario':'testapi@test.xyz', 'senha':'simples'}, extra={'accept':'application/json'})
        #print("Response code: ", response.content)
        self.assertContains(response= response,text='testapi@test.xyz', status_code=200 )
        pass

    def test_2_procura_cadastro_por_usuario(self):
        QuerySet(model=Cadastro).create(usuario='testapi@test.xyz', senha='simples')
        response = self.client.get('/cadastro/usuario/inscrito/', data={'usuario':'testapi@test.xyz'})
        self.assertContains(response, status_code=200, text='testapi@test.xyz') #("Response code_2: ", response.status_code)
        pass

    def test_3_procura_cadastros_por_estado(self):
        """Testa a pesquisa de cadastros por estado
        """
        cadastros = [
            Cadastro(usuario='testapi1@test.xyz', senha='simples'),
            Cadastro(usuario='testapi2@test.xyz', senha='simples'),
            Cadastro(usuario='testapi3@test.xyz', senha='simples')
        ]
        QuerySet(model=Cadastro).bulk_create(cadastros)
        response = self.client.get('/cadastro/usuarios/', data={'estado':'PENDENTE'})
        #print("Response code_3: ", response.content)
        self.assertContains(response=response, status_code=200, text=3) 
        pass

    def test_4_modifica_estado_cadastro(self):
        """Testa a atualizacao de estado do cadastro  
        """
        QuerySet(model=Cadastro).create(usuario='testapi1@test.xyz', senha='simples')
        response = self.client.post('/cadastro/usuario/estado/', data={'usuario':'testapi1@test.xyz', 'estado':'ATIVO'})
        self.assertContains(response=response, text=1, status_code=200)
        

    def test_5_renova_senha(self):
        """Testa a renovacao da palavra-passe
        """
        QuerySet(model=Cadastro).create(usuario='testapi@test.xyz', senha='simples')
        response = self.client.post('/cadastro/usuario/senha/', data={'usuario':'testapi@test.xyz', 'senha':'simples+diferente'})
        self.assertContains(response=response, text=1, status_code=200)