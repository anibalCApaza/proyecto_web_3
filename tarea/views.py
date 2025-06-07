from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def ver_tarea(request, id):
    return HttpResponse(
        b"Esta vista muestra la informacion de una tarea con id x, puede reemplazarse por un modal en la vista de ver_proyecto si se prefiere"
    )


def crear_tarea(request):
    return HttpResponse(
        b"Esta vista muestra un formulario en caso de una peticion GET, si es POST valida los datos de la nueva tarea y la registra, es importante considerar que entre estos datos debe figurar el id del proyecto al que se agregara esta tarea"
    )


def crear_etiqueta(request):
    return HttpResponse(
        b"Esta vista muestra un formulario en caso de una peticion GET, si es POST valida los datos de la nueva etiqueta y la registra, es importante considerar que entre estos datos debe figurar el id de la tarea al que se agregara esta etiqueta"
    )
