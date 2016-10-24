from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, payment_was_flagged


def payment_signal(sender, **kwargs):
    ipn_object = sender
    if ipn_object.payment_status == ST_PP_COMPLETED:
        print "payment_status == ST_PP_COMPLETED"

        """
        Here use django-registration to authenticate
        the User
        """

    else:
        print str(ipn_object.payment_status)
        print "error"

valid_ipn_received.connect(payment_signal)
payment_was_flagged.connect(payment_signal)

print "SIGNALS MODULE IMPORTED"