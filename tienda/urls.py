from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_productos, name='lista_productos'),
    url(r'^(?P<slug_categoria>[-\w]+)/$', views.lista_productos, name="lista_productos_por_categoria"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detalles_producto, name="detalles_producto"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
