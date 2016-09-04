from django.db import models

# Create your models here.


class OAT(models.Model):

    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, blank=True)
    src_image = models.CharField(max_length=255)
    pass

class Curso(models.Model):

    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_fin = models.DateTimeField(blank=True)
    oats = models.ForeignKey(OAT)
