from django.shortcuts import render
from .models import ItemPedido
from .forms import FormCreaPedido
from carro_compras.carro_compras import Carro
from .tasks import pedido_creado

def crear_pedido(request):
	carro = Carro(request)
	if request.method == 'POST':
		form = FormCreaPedido(request.POST)
		if form.is_valid():
			pedido = form.save()
			for item in carro:
				ItemPedido.objects.create(pedido=pedido, producto=item['producto'], precio=item['precio'], cantidad=item['cantidad'])
			carro.limpiar()
			pedido_creado.delay(pedido.id)
			return render(request, 'pedidos/pedido/creado.html', {'pedido':pedido})
	else:
		form = FormCreaPedido()
		return render(request, 'pedidos/pedido/crear.html', {'carro':carro, 'form':form})