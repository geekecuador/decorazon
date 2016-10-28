# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from social.pipeline import user
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from .models import Donaciones,Codigo,Proyecto
from paypal.standard.forms import PayPalPaymentsForm
from django.core.exceptions import ObjectDoesNotExist
from decorazon import settings
# Create your views here.
from landing.models import UserProfile
from twython import Twython
import time



@csrf_exempt
def mashcaindex(request):
    host = request.get_host()
    invoice = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%y")
    TWITTER_APP_KEY = 'O8eDCWgXvylYlGabAci93ppd7'  # supply the appropriate value
    TWITTER_APP_KEY_SECRET = 'pILt8uKye8rKgJTjYCsTX6z8Vv6zBsXacCBkyqOjbGr7srz0bm'
    TWITTER_ACCESS_TOKEN = '52223076-Lz9IZxqNFhURxgK9cvAWTwxmHg25saSKPoHxwizml'
    TWITTER_ACCESS_TOKEN_SECRET = 'yz5KMoSSripHbqH23zlvg7WeZVdsFXLcU7JyxOXU2ccRE'

    twitter = Twython(app_key=TWITTER_APP_KEY,
                app_secret=TWITTER_APP_KEY_SECRET,
                oauth_token=TWITTER_ACCESS_TOKEN,
                oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    results = twitter.search(q='#mashcadecorazon',  # **supply whatever query you want here**
                      count=5)
    tweets = results['statuses']
    comentarios = []
    imagenes_perfil = []
    for tweet1 in tweets:
        tweet1['text'] = Twython.html_for_tweet(tweet1)
        comentarios.append(tweet1['text'])
        imagenes_perfil.append('https://twitter.com/'+tweet1['user']['screen_name']+'/profile_image?size=original')

    pry = Proyecto.objects.get(clave="MASHC")
    porcentaje = int((pry.cantidadalcanzada * 100)/pry.cantidadbase)
    ano = '2016 '
    comentarios_twitter = zip(comentarios, imagenes_perfil)
    pepe = 0
    donantes = Donaciones.objects.all().count()
    mensaje = ''
    print pry.fecha_limite.year
    if request.method == 'POST':
        codigo = request.POST.get('input_text')
        try:
            codifo_verificar = Codigo.objects.get(codigo=codigo)
            global valor
            valor = codifo_verificar.valor
            if codifo_verificar.activo:
                donacion = Donaciones(usuario=request.user, codigo=codifo_verificar)
                donacion.save()
                if donacion.id:
                    pepe = 2
                    codifo_verificar.activo = False
                    codifo_verificar.save()
                else:
                    mensaje = "Hubo un problema en el registro, envienos a ddd@dd.com su codigo para la verificacion"
                    pepe = 1
            else:
                mensaje = "El codigo ingresado ya fue usado."
                pepe = 1
        except ObjectDoesNotExist:
            mensaje =  "Codigo no existe"
            pepe = 1

    if request.user.is_authenticated():
        x = UserProfile.objects.get(user=request.user)
        paypal_dict5 = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": "5.00",
            "item_name": "Mashca de Corazón $5",
            "invoice": invoice,
            'currency_code': 'USD',
            "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        paypal_dict10 = {
            "business":   settings.PAYPAL_RECEIVER_EMAIL,
            "amount": "10.00",
            "item_name": "Mashca de Corazón $10",
            "invoice": invoice,
            'currency_code': 'USD',
               "notify_url": 'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        paypal_dict20 = {
            "business": "mashcadecorazon@gmail.com  ",
            "amount": "20.00",
            "item_name": "Mashca de Corazón $20",
            "invoice": invoice,
            'currency_code': 'USD',
            "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        paypal_dict100 = {
            "business": "mashcadecorazon@gmail.com  ",
            "amount": "100.00",
            "item_name": "Mashca de Corazón $100",
            "invoice": invoice,
            'currency_code': 'USD',
            "notify_url": 'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        paypal_dict500 = {
            "business": "mashcadecorazon@gmail.com  ",
            "amount": "500.00",
            "item_name": "Mashca de Corazón $500",
            "invoice": invoice,
            'currency_code': 'USD',
            "notify_url": 'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        paypal_dict1000 = {
            "business": "mashcadecorazon@gmail.com  ",
            "amount": "1000.00",
            "item_name": "Mashca de Corazón $1000",
            "invoice": invoice,
            'currency_code': 'USD',
            "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('mashca:payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('mashca:payment_canceled')),
            "custom": x.user.username,

        }
        # Create the instance.
        form5 = PayPalPaymentsForm(initial=paypal_dict5)
        form10 = PayPalPaymentsForm(initial=paypal_dict10)
        form20 = PayPalPaymentsForm(initial=paypal_dict20)
        form100 = PayPalPaymentsForm(initial=paypal_dict100)
        form500 = PayPalPaymentsForm(initial=paypal_dict500)
        form1000 = PayPalPaymentsForm(initial=paypal_dict1000)
        try:
            return render(request, 'jocha.html',
                          {'ano': ano, 'user': request.user, 'donantes': donantes,'comentarios_twitter':comentarios_twitter,'imagenes_perfil':imagenes_perfil,'comentarios':comentarios, 'porcentaje': porcentaje,
                           'mensaje': mensaje, 'photo': x.image_file, 'form10': form10,
                           'form5': form5,'form20': form20,'form100': form100,'form500': form500,
                           'form1000': form1000,
                           'pepe': pepe,
                           'valor': valor, 'pry': pry},
                          content_type='text/html')
        except Exception:
            return render(request, 'jocha.html',
                          {'ano': ano, 'user': request.user, 'pry': pry,'imagenes_perfil':imagenes_perfil,'comentarios':comentarios, 'porcentaje': porcentaje, 'donantes': donantes,
                           'photo': x.image_file, 'form10': form10,
                           'form5': form5,'form20': form20,'form100': form100,'form500': form500,
                           'form1000': form1000,
                           'donantes': donantes, 'pepe': pepe,'comentarios_twitter':comentarios_twitter,
                           },
                          content_type='text/html')

    else:
        return render(request, 'jocha.html', {'donantes': donantes,'comentarios_twitter':comentarios_twitter,'imagenes_perfil':imagenes_perfil,'comentarios':comentarios,'pry':pry,'porcentaje':porcentaje}, content_type='text/html')


def logout(request):
    auth_logout(request)
    return redirect('/mashca/')


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def gallery(request):
    lista_url = []
    try:
        donantes = Donaciones.objects.filter(codigo__proyecto__clave='MASHC')
        for persona in donantes:
            imagen_usuario = UserProfile.objects.get(user=persona.usuario)
            imagen_url = imagen_usuario.image_url
            lista_url.append(imagen_url)
        return render(request,'gallery.html',{'lista_url':lista_url},content_type='text/html')
    except ObjectDoesNotExist:
        return render(request,'gallery.html',{'lista_url':lista_url},content_type='text/html')


