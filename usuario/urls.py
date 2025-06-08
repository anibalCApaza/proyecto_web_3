from django.urls import path

from . import views


app_name = "usuario"
urlpatterns = [
    path("registrarse/", views.registrarse, name="registrarse"),
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("mostrar_usuario/", views.mostrar_usuario, name="cerrar_sesion"),
]
