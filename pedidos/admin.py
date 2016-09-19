from django.contrib import admin
from .models import Pedido, ItemPedido

class LineaItemPedido(admin.TabularInline):
	model = ItemPedido
	raw_id_fields = ['producto']

class PedidoAdmin(admin.ModelAdmin):
	list_display = ['id','nombre','apellido','email','direccion','pago','fecha_creacion','fecha_modificacion']
	list_filter = ['pago','fecha_creacion','fecha_modificacion'] 
	inlines = [LineaItemPedido]

admin.site.register(Pedido, PedidoAdmin)