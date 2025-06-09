from django.db import models
from proyecto.models import Proyecto
from django.contrib.auth.models import User


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    relevancia = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
