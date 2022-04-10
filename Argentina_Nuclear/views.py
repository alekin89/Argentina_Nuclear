from contextvars import Context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Bienvenidos a Argentina Nuclear")

def segunda_vista(request):
    return HttpResponse("<br><br>En esta página hay información sobre instalaciones nucleares en Argentina")

def miapellidoes(self, apellido):
    docdetexto = f"Mi apellido es: <br><br> {apellido}"
    return HttpResponse(docdetexto)

def probandotemplate(self):
    
    cen = "Atucha"
    num = "I"
    
    diccionario = {"central":cen,"numero":num}
    
    #miHtml = open("C:/Users/aleki/OneDrive/Escritorio/Curso Python/Django/TrabajoFinal/Argentina_Nuclear/Argentina_Nuclear/Plantillas/Template1.html")
    #plantilla = Template(miHtml.read())  
    #miHtml.close()
    #micontexto=Context(diccionario)
    #documento=plantilla.render(micontexto)
    #return HttpResponse(documento)
    
    plantilla = loader.get_template('Template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)