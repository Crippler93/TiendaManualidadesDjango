from celery import task
from django.core.mail import send_mail
from .models import Pedido

@task
def pedido_creado(pedido_id):
	pedido = Pedido.objects.get(id=pedido_id)
	subject = 'Pedido nro. {}'.format(pedido.id)
	message = 'Querido {}, \n\nTu pedido fue exitosamente registrado. El id de tu pedido es {}.'.format(pedido.nombre,pedido.id)
	mail_sent = send_mail(subject, message, 'admin@TiendaManualidades.com', [pedido.email], fail_silently=False,)
	return mail_sent
