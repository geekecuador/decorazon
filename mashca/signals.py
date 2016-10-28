from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

from django.contrib.auth.models import User
from models import Donacion_Paypal

def payment_notification(sender, **kwargs):
    print "Estamos en el signals"
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        print "Grabado la donacion paypal"
        user = User.objects.filter(username=ipn_obj.custom)
        donacion = Donacion_Paypal(usuario=user, valor=ipn_obj.amount)
        donacion.save()
valid_ipn_received.connect(payment_notification)

