from decimal import Decimal
from django.conf import settings
from tienda.models import Producto

class Carro(object):

	def __init__(self, request):
		self.session = request.session
		carro = self.session.get(settings.CART_SESSION_ID)
		if not carro:
			carro = self.session[settings.CART_SESSION_ID] = {}
		self.carro = carro

	def adicionar(self, producto, cantidad=1, actualiza_cantidad=False):
		producto_id = str(producto.id)
		if producto_id not in self.carro:
			self.carro[producto_id] = {'cantidad':0,'precio': str(producto.precio)}

		if actualiza_cantidad:
			self.carro[producto_id]['cantidad'] = cantidad
		else:
			self.carro[producto_id]['cantidad'] += cantidad
		self.guardar()

	def guardar(self):
		self.session[settings.CART_SESSION_ID] = self.carro
		self.session.modified = True

	def remover(self, producto):
		producto_id = str(producto.id)
		if producto_id in self.carro:
			del self.carro[producto_id]
			self.guardar()

	def __iter__(self):
		producto_ids = self.carro.keys()
		productos = Producto.objects.filter(id__in=producto_ids)
		for producto in productos:
			self.carro[str(producto.id)]['producto'] = producto

		for item in self.carro.values():
			item['precio'] = Decimal(item['precio'])
			item['precio_total'] = item['precio'] * item['cantidad']
			yield item

	def __len__(self):
		return sum(item['cantidad'] for item in self.carro.values())

	def obtener_precio_total(self):
		return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())

	def limpiar(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True