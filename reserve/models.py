from django.db import models

# Create your models here.

class ClienteModels(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=50)
    telefono = models.PositiveBigIntegerField()
    
    def __str__(self) -> str:
        texto = '{0} {1} {2} {3} {4}'
        return texto.format(self.nombre,self.apellido,self.edad,self.email,self.telefono)
    
class ServicioModels(models.Model):
    nombre = models.CharField(max_length=150)
    capacidad = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        texto = '{0} {1} {2}'
        return texto.format(self.nombre,self.capacidad,self.disponibilidad)
    
class ReservaModels(models.Model):
    cliente = models.ForeignKey(ClienteModels, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioModels, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self) -> str:
        return f"Reserva para el cliente {self.cliente} para el {self.servicio}"