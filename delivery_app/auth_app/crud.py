#Pra seguir os princípios solid vou separar as funções, repositories agora vai ser responsável pela comunicação com o banco de dados, percebi que não posso colocar as regras de negócio junto das views, isso deixa meu código nojento e desorganizado 

"""O que é um Método Estático?
Um método estático em Python é um método que pertence a uma classe, mas não está associado a nenhuma instância da classe. Ele não pode acessar ou modificar o estado da instância da classe, ou seja, ele não pode acessar self ou cls. Ele é definido usando o decorador @staticmethod.

Por que Usar Métodos Estáticos em Repositórios?
Não Dependem do Estado da Instância: Métodos estáticos são ideais para operações que não dependem do estado da instância da classe. Em repositórios, frequentemente, os métodos realizam operações de CRUD que não necessitam de um estado específico da classe.

Organização e Estrutura: Mesmo que os métodos não dependam do estado da instância, agrupá-los em uma classe pode ajudar a organizar e estruturar o código de maneira lógica. Isso pode tornar o código mais fácil de entender e manter.

Acesso Direto: Métodos estáticos podem ser chamados diretamente na classe sem precisar criar uma instância da classe. Isso pode ser útil para evitar a criação de objetos desnecessários, economizando recursos."""


#Esse aqui é o arquivo CRUD do nosso app auth, ou seja, responsável pelas tarefas de CREATE READ UPDATE DELETE (CRUD)

from auth_app.models import DeliverymanModel as DM, ClientModel as CM, RestaurantModel as RM, User

class UserRepository:
    @staticmethod
    def create_user(username, email, password):
        #cria um novo usuario
        return User.objects.create_user(username=username, email=email, password=password)
    
    """@staticmethod
    def get_user_by_username(username):
        #Busca um usuário pelo nome de usuário.
        return User.objects.filter(username=username).first()"""
#-----------------------------------------------------------------------------------------------------------------------
    
class UserTypeRepository:
    @staticmethod
    def create_user_type(user, user_type):
        """cria um novo tipo de usuário."""
        return User.objects.create(user=user, user_type=user_type)
#-----------------------------------------------------------------------------------------------------------------------

class DeliverymanRepository:
    @staticmethod
    def create_deliveryman(profile):
        """cria um deliveryman."""
        return DM.objects.create(profile=profile)
    
    """@staticmethod
    def get_deliveryman_by_username(username):
        #Busca um deliveryman pelo nome de usuário.
        username=DM.perfil.username
        return DM.objects.filter(username=username).first()"""
    
class ClientRepository:
    @staticmethod
    def create_client(profile):
        """cria um cliente."""
        return CM.objects.create(profile=profile)
    
    """ @staticmethod
        def get_client_by_username(username):
            #Busca um usuário pelo nome de usuário.
            username=CM.perfil.username
            return CM.objects.filter(username=username).first()"""
        

#-----------------------------------------------------------------------------------------------------------------------
    
class RestaurantRepository:
    @staticmethod
    def create_restaurant(profile):
        """cria um restautante."""
        return RM.objects.create(perfil=profile)
    
    """@staticmethod
    def get_restaurant_by_username(username):
        #Busca um restaurante pelo nome de usuário.
        username=RM.perfil.username
        return RM.objects.filter(username=username).first()"""
