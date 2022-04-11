from django.urls import path
from AppNucleo import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('centrales', views.centrales, name="Centrales"),
    path('reactores', views.reactores, name="Reactores"),
    path('fabricas', views.fabricas, name="Fabricas"),
    #path('centralesformulario', views.centralesformulario, name="Centralesformulario"),
    path('fabricasformulario', views.fabricasformulario, name="Fabricasformulario"),
    path('reactoresformulario', views.reactoresformulario, name="Reactoresformulario"),
    path('busquedaUbicacion', views.busquedaUbicacion, name="BusquedaUbicacion"),
    path('resultadosBusqueda', views.buscar, name='resultadosBusqueda'),
    path('buscar/', views.buscar),
]