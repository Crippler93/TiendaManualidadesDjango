from django.contrib import admin
from .models import Categoria, Producto, Imagen

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','slug']
    prepopulated_fields = {'slug':('nombre',)}
admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio', 'stock', 'disponible', 'fecha_creacion', 'fecha_actualizacion']
    list_filter = ['disponible','fecha_creacion','fecha_actualizacion']
    list_editable = ['precio','stock','disponible']
    prepopulated_fields = {'slug': ('nombre',)}
admin.site.register(Producto,ProductoAdmin)

admin.site.register(Imagen)