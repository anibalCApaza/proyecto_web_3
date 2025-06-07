from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    usuario_creado = models.ForeignKey(User, on_delete=models.CASCADE)
