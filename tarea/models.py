from django.db import models
from proyecto.models import Proyecto
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    name = models.CharField("Nombre del proyecto", max_length=100)
    description = models.TextField("Descripción", blank=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator_team"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("TODO", "Pendiente"),
        ("IN_PROGRESS", "En progreso"),
        ("DONE", "Completada"),
    ]

    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descripción", blank=True)
    status = models.CharField(
        "Estado", max_length=20, choices=STATUS_CHOICES, default="TODO"
    )
    project = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Proyecto")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator_task"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title


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
