from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.\
from .models import Contacto
def index(request):
    ano = '2016 '
    mensaje = False
    if request.method == 'POST':
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        tema = request.POST.get('subject')
        mensaje = request.POST.get('comments')
        contacto = Contacto(nombre=nombre,email=email,tema=tema,mensaje=mensaje)
        if (contacto.save()):
            mensaje = True
    return render(request,'index.html',{'ano':ano,'mensaje':mensaje})
