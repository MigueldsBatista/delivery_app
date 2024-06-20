from rolepermissions.roles import AbstractUserRole

class Restaurante(AbstractUserRole):
    available_permissions = {
        'ver_pedidos': True,
        'ver_estatisticas': True
    }

class Entregador(AbstractUserRole):
    available_permissions = {
        'ver_pedidos': True
    }


class Cliente(AbstractUserRole):
    available_permissions = {
        'fazer_pedidos': True
    }
