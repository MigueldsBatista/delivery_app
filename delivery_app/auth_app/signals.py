from django.db.models.signals import post_save
from .models import User
from .crud import ClientRepository as CR, UserTypeRepository as UR, RestaurantRepository as RR, DeliverymanRepository as DR

from django.db.models.signals import post_save


def create_user_signal(sender, instance, created, **kwargs):
    print('sinal chamado com sucesso')
    if created:
        if instance.user_type == 'entregador':
            DR.create_deliveryman(instance)
        elif instance.user_type == 'restaurante':
            RR.create_restaurant(instance)
        elif instance.user_type == 'cliente':
            CR.create_client(instance)
        UR.create_user_type(instance, instance.user_type)

post_save.connect(create_user_signal, sender=User)
