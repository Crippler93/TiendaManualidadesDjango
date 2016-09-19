from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tienda.models import Producto
from .carro_compras import Carro
from .forms import FormAdicionarProductoCarro

@require_POST
def adicionar_carro(request, producto_id):
	carro = Carro(request)
	producto = get_object_or_404(Producto, id=producto_id)
	form = FormAdicionarProductoCarro(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		carro.adicionar(producto=producto,cantidad=cd['cantidad'],actualiza_cantidad=cd['actualizar'])
	return redirect('carro_compras:detalle_carro')

def remover_carro(request, producto_id):
	carro = Carro(request)
	producto = get_object_or_404(Producto, id=producto_id)
	carro.remover(producto)
	return redirect('carro_compras:detalle_carro')

def detalle_carro(request):
	carro = Carro(request)
	return render(request, 'carro/detalle.html', {'carro':carro})
