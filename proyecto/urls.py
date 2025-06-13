from django.urls import path
from . import views

app_name = "proyecto"
urlpatterns = [
    path(
        "index/", views.index, name="index"
    ),  # Única url accesible para usuarios no logueados
    path("lista/", views.lista_proyecto, name="lista_proyectos"),
    path("crear/", views.crear_proyecto, name="crear_proyecto"),
    path("ver/<int:id>", views.ver_proyecto, name="ver_proyecto"),
    path("agregar_usuario/<int:id>",views.agregar_usuario,name="agregar_usuario")
]
