from django.http import HttpResponse
from django.shortcuts import render

# Considera que todas las views deben mostrar html, por que se tiene que usar return render.........


def registrarse(request):
    return HttpResponse(
        b"Esta vista debe mostrar un formulario de registro en caso de ser una solicitud GET, si es solicitud POST debe validar los datos de registro y crear el usuario en la base de datos(usuario normal. sin privilegios ni ningun rol administrativo), iniciar sesion y mandar a proyecto/index"
    )


def iniciar_sesion(request):
    return HttpResponse(
        b"Esta vista debe mostrar un formulario de inicio de sesion en caso de ser una solicitud GET, si es solicitud POST debe validar los datos de acceso(username y password), iniciar sesion y mandar a proyecto/index"
    )


def cerrar_sesion(request):
    return HttpResponse(b"Esta vista debe cerrar la sesion y mandar a proyecto/index")
