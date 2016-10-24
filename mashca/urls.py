from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.mashcaindex, name='mashcaindex'),
    url(r'^gallery/$', views.gallery, name='mashcagallery'),
    url(r'^logout/$', views.logout, name='mashcalogout'),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^pago/$', include('paypal.standard.ipn.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)