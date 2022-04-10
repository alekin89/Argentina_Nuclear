from django.db import models

# Create your models here.
class centrales(models.Model):
    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=30)
    cant_EC=models.IntegerField() #Cantidad de elementos combustibles de la central
    inicio=models.DateField() #Fecha de inauguración

class reactores(models.Model):
    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=30)
    activo=models.BooleanField() #Para indicar si el reactor funciona en la actualidad o no

class fabricas(models.Model):
    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=30)
    empleados=models.IntegerField() #Numero de empleados
    