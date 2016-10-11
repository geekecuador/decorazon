from django import forms
from .models import Contacto
class ContactoFormulario(forms.Form):
    class Meta:
        model = Contacto
        fields = ['nombre','email','tema','mensaje']

