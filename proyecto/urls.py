from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.lista_proyecto, name="lista_proyectos"),
    path("crear/", views.crear_proyecto, name="crear_proyecto"),
    path("ver/<int:id>", views.ver_proyecto, name="ver_proyecto"),
]
