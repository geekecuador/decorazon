from django.contrib import admin
from .models import Codigo, Proyecto,  Donaciones
# Register your models here.
admin.site.register(Codigo)
admin.site.register(Proyecto)
admin.site.register(Donaciones)