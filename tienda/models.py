from django.db import models
from django.core.urlresolvers import reverse
from stdimage import StdImageField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tienda:lista_productos_por_categoria', args=[self.slug])

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='categorias')
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d',blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField('Producto Disponible', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Fecha de Actualzacion', auto_now=True)

    class Meta:
        ordering = ('nombre',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('tienda:detalles_producto', args=[self.id,self.slug])

class Imagen(models.Model):
    imagen = StdImageField(upload_to='slider/%Y/%m/%d',blank=True, variations={'large': (1200, 480)})

    def __str__(self):
        return self.imagen.url