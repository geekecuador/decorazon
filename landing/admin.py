from django.contrib import admin
from .models import Contacto,UserProfile
from django.contrib.admin import DateFieldListFilter
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_filter = (('date_field_name',DateFieldListFilter),)

