from django.contrib import admin
from .models import Codigo, Proyecto,  Donaciones,Donacion_Paypal
# Register your models here.
admin.site.register(Codigo)
admin.site.register(Proyecto)
admin.site.register(Donaciones)
admin.site.register(Donacion_Paypal)