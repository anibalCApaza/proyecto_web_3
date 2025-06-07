from django.urls import path
from tarea import views


urlpatterns = [
    path("ver_tarea/<int:id>", views.ver_tarea, name="ver_tarea"),
    path("crear_tarea/", views.crear_tarea, name="crear_tarea"),
    path("crear_etiqueta/", views.crear_etiqueta, name="crear_etiqueta"),
]
