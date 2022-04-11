from django import forms

class Centralesformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    ubicacion=forms.CharField(max_length=30)
    cant_EC=forms.IntegerField() #Cantidad de elementos combustibles de la central

class Reactoresformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    ubicacion=forms.CharField(max_length=30)
    activo=forms.BooleanField() #Para indicar si el reactor funciona en la actualidad o no

class Fabricasformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    ubicacion=forms.CharField(max_length=30)
    empleados=forms.IntegerField() #Numero de empleados