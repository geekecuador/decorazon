from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    tema = models.CharField(max_length=30)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.nombre + " " +self.email