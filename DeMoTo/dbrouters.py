#Criar as rota para os modelos dos aplicativos
#Roteador para o modelo usuario basico
class UsuarioRouter:
    
    def __init__(self):
        self.rota_app_label = {'usuario'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de leitura do modelo usuario serao encaminhados para a base de dados usuarios. Caso contrario, retorna nulo
        Args:
            model: referencia do modelo na variable DATABASES_ROUTERS das definicoes (settings.py);
        Retorno:
            string: nome (aliais) da base de dados definida no variabel DATABASES das definicoes (settings.py)
            Nenhum: 
        """
        if model._meta.app_label in self.rota_app_label:
            return 'usuarios'
        return None

    def db_for_write (self, model, **hints):
        """
        Encaminhas as tentativas de escrita do modelo usuario para a base de dados usuarios. caso contrario, retorna nulo
        """
        if model._meta.app_label in self.rota_app_label:
            return 'usuarios'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints ):
        """
        Assegurar que todas migracoes do modelo usuario e relacionados sao encaminhadas para a base de dados usuarios.
        """