from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, Imagen
from carro_compras.forms import FormAdicionarProductoCarro


# Create your views here.

def lista_productos(request, slug_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    imagenes = Imagen.objects.all()
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        productos = productos.filter(categoria=categoria)
    return render(request, 'tienda/producto/lista.html', {'categoria':categoria, 'categorias':categorias, 'productos':productos, 'imagenes':imagenes})

def detalles_producto(request, id, slug):
    producto = get_object_or_404(Producto, id=id, slug=slug, disponible=True)
    form_producto_carro = FormAdicionarProductoCarro()
    return render(request, 'tienda/producto/detalle.html', {'producto':producto,'form_producto_carro':form_producto_carro})    
    
