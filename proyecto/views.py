from django.http import HttpResponse
from django.shortcuts import render

# TODO: Considera que todas las vistas deben usar return render....... para mostrar su información en un template


def index(request):
    return HttpResponse(
        b"Esta vista retorna el index por defecto de todo el proyecto, que muestra la descripcion del proyecto, el unico accesible para usuarios no logueados"
    )


def lista_proyecto(request):
    return HttpResponse(
        b"Esta vista debe mostrar la lista de proyectos, podria ser en una tabla por ejemplo"
    )


def crear_proyecto(request):
    return HttpResponse(
        b"Esta vista debe mostrar un formulario si el metodo de acceso es GET, si es POST debe validar los datos de un posible proyecto, registrarlo y mandarnos a lista_proyecto"
    )


def ver_proyecto(request):
    return HttpResponse(
        b"Esta vista debe mostrar la informacion de un proyecto de x id, incluyendo el nombre de propietario, nombre de miembros, listado de tareas y las etiquetas de cada tarea"
    )
