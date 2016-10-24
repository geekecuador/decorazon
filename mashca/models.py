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
    video = models.FileField(upload_to=u'video/', max_length=200)

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




def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    if ipn_obj.custom == "Upgrade all users!":
        print "DAVID "
payment_was_successful.connect(show_me_the_money)