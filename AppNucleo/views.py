from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppNucleo.models import Centrales, Reactores, Fabricas
from AppNucleo.forms import Centralesformulario, Reactoresformulario, Fabricasformulario

# Create your views here.
def inicio(request):
    return render(request, "AppNucleo/inicio.html")

def centrales(request):
    return render(request, "AppNucleo/centrales.html")

def reactores(request):
    return render(request, "AppNucleo/reactores.html")

def fabricas(request):
    return render(request, "AppNucleo/fabricas.html")



def centrales(request):
    if request.method == 'POST':
        cenformulario=Centralesformulario(request.POST)
        print(cenformulario)
        
        if cenformulario.is_valid:
            informacion=cenformulario.cleaned_data
            print(informacion)
            centrales = Centrales(nombre=informacion['nombre'], ubicacion=informacion['ubicacion'], cant_EC=informacion['cant_EC'])
            centrales.save()
            
            return render(request, "AppNucleo/inicio.html")
        
    else:
        
        cenformulario = Centralesformulario()
        
    return render(request, "AppNucleo/centrales.html", {"cenformulario":cenformulario})



           
def reactoresformulario(request):
    
    if request.method == 'POST':
        reactformulario=Reactoresformulario(request.POST)
        print(reactformulario)
        
        if reactformulario.is_valid:
            informacion=reactformulario.cleaned_data
            print(informacion)
            reactores = Reactores(nombre=informacion['nombre'], ubicacion=informacion['ubicacion'], activo=informacion['activo'])
            reactores.save()
            
            return render(request, "AppNucleo/inicio.html")
        
    else:
        
        reactformulario = Reactoresformulario()
        
    return render(request, "AppNucleo/reactoresformulario.html", {"reactformulario":reactformulario})



def fabricasformulario(request):
    
    if request.method == 'POST':
        fabformulario=Fabricasformulario(request.POST)
        print(fabformulario)
        
        if fabformulario.is_valid:
            informacion=fabformulario.cleaned_data
            print(informacion)
            fabricas = Fabricas(nombre=informacion['nombre'], ubicacion=informacion['ubicacion'], empleados=informacion['empleados'])
            fabricas.save()
            
            return render(request, "AppNucleo/inicio.html")
        
    else:
        
        fabformulario = Fabricasformulario()
        
    return render(request, "AppNucleo/fabricasformulario.html", {"fabformulario":fabformulario})




def busquedaUbicacion(request):
    
    return render(request, "AppNucleo/busquedaUbicacion.html")


def buscar(request):
    
    if request.GET["ubicacion"]:
        
        ubicacion = request.GET['ubicacion']
        reactores = Reactores.objects.filter(ubicacion__icontains=ubicacion)
        
        return render(request, "AppNucleo/resultadosBusqueda.html", {"reactores":reactores, "ubicacion":ubicacion})
    
    else:
        
        respuesta = "No enviaste datos"
    
    #respuesta = f"Estoy buscando la ubicacion de: {request.GET['ubicacion']}"
    
    return HttpResponse(respuesta)