from django.db import models
from stdimage import StdImageField

class Post(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	imagen = StdImageField(upload_to='post/%Y/%m/%d',blank=True, variations={'large': (640, 480), 'thumbnail': (100, 100)})
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-fecha_creacion',)

	def __str__(self):
		return self.titulo