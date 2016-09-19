from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.detalle_carro, name='detalle_carro'),
	url(r'^adicionar/(?P<producto_id>\d+)/$', views.adicionar_carro, name='adicionar_carro'),
	url(r'^remover/(?P<producto_id>\d+)/$', views.remover_carro, name='remover_carro'),
]