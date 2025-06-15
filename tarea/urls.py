from django.urls import path
from tarea import views


urlpatterns = [
    path("ver_tarea/<int:id>", views.ver_tarea, name="ver_tarea"),
    path("crear_tarea/<int:id_proyecto>", views.crear_tarea, name="crear_tarea"),
    path("crear_etiqueta/", views.crear_etiqueta, name="crear_etiqueta"),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('agregar_Etiqueta/<int:tarea_id>/', views.agregar_etiqueta, name='agregar_etiqueta'),
    path('<int:tarea_id>/asignar/', views.asignar_tarea, name='asignar_tarea'),
    path('editar_tarea/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
]
