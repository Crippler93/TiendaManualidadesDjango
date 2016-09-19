from .carro_compras import Carro

def carro(request):
	return {'carro': Carro(request)}