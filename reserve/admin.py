from django.contrib import admin
from .models import ClienteModels,ServicioModels,ReservaModels

# Register your models here.
admin.site.register(ClienteModels)
admin.site.register(ServicioModels)
admin.site.register(ReservaModels)
