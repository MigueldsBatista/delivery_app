from django.db import models
from django.contrib.auth.models import AbstractUser

#Estamos criando aqui os modelos dos diferentes tipos de usuario
#Pra melhorar o inglês tambem vou nomear as variaveis em ingles, as instruções por motivos de que alguem pode ler isso, vão ficar em português pra melhorar a legibilidade

#Lógica um pouco complicada no inicio mas melhora o encapsulamento

class User(AbstractUser):
    user_type=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_type}'

class DeliverymanModel(models.Model):
    profile=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.username}'

class ClientModel(models.Model):
    profile=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.username})'

class RestaurantModel(models.Model):
    profile=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.username}'