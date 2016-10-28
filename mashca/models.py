from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from paypal.standard.ipn.signals import payment_was_successful

class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    clave = models.CharField(max_length=5)
    cantidadbase = models.DecimalField(max_digits=8, decimal_places=2)
    cantidadalcanzada = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_limite = models.DateTimeField()

    def __str__(self):
        return self.nombre


class Codigo(models.Model):
    codigo = models.CharField(max_length=15)
    proyecto = models.ForeignKey(Proyecto)
    valor = models.PositiveIntegerField()
    activo = models.BooleanField(auto_created=True)

    def __str__(self):
        return self.codigo + " - " + self.proyecto.nombre + " - " + str(self.valor)


class Donaciones(models.Model):
    usuario = models.ForeignKey(User)
    codigo = models.ForeignKey(Codigo)

    def __str__(self):
        return self.usuario.username + self.codigo.codigo

class Donacion_Paypal(models.Model):
    usuario = models.ForeignKey(User)
    valor = models.CharField(max_length=10)

    def __str__(self):
        return self.usuario.username + self.valor
