from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'Pendiente'),
        ('IN_PROGRESS', 'En progreso'),
        ('DONE', 'Completada'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')

    def get_status_class(self):
        if self.status == 'DONE':
            return 'success'
        elif self.status == 'IN_PROGRESS':
            return 'warning'
        return 'secondary'



class Team(models.Model):  # Modelo para proyectos
    name = models.CharField("Nombre del proyecto", max_length=100)
    description = models.TextField("Descripción")
    start_date = models.DateField("Fecha de inicio")  
    end_date = models.DateField("Fecha de fin")       
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)


class MiembroProyecto(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario_agregado = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="usuario_agregado_a_proyecto"
    )
