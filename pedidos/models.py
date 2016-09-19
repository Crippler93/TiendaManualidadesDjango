from django.db import models
from tienda.models import Producto

class Pedido(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	email = models.EmailField()
	direccion = models.CharField(max_length=100)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	pago = models.BooleanField(default=False)

	class Meta:
		ordering = ('-fecha_creacion',)

	def __str__(self):
		return 'Pedido {}'.format(self.id)

	def obtener_costo_total(self):
		return sum(item.obtener_costo() for item in self.items.all())

class ItemPedido(models.Model):
	pedido = models.ForeignKey(Pedido, related_name='items')
	producto = models.ForeignKey(Producto, related_name='items_pedidos')
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	cantidad = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def obtener_costo(self):
		return self.precio * self.cantidad		
