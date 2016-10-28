from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='mashcalogout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)