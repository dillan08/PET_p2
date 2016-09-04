from django.db import models
from Manejador_OATs.models import OAT
# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(auto_now_add=False)
    noAlumnos = models.IntegerField()
    alumnos = models.ForeignKey(OAT)
