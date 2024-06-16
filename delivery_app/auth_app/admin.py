from django.contrib import admin
from .models import * #Importando todos os modelos

admin.site.register(EntregadorModel)
admin.site.register(ClienteModel)
admin.site.register(RestauranteModel)
