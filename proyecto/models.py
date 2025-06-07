from django.db import models
from django.contrib.auth.models import User


# Create your models here.


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
