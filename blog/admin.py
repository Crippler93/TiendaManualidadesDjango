from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['titulo','imagen','fecha_modificacion','fecha_creacion']
	list_filter = ['titulo','fecha_modificacion','fecha_creacion']

admin.site.register(Post, PostAdmin)