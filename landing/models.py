from __future__ import unicode_literals
import urllib
from django.db import models
import os
from django.contrib.auth.models import User
from django.core.files import File

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    tema = models.CharField(max_length=30)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha"]
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre + " " + self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to='ProyectMashca/images', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            result = urllib.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url + '.jpg'),
                File(open(result[0]))
            )
            self.save()
        super(UserProfile, self).save(*args, **kwargs)
