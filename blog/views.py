from django.shortcuts import render
from .models import Post

def lista_post(request):
	posts = Post.objects.all()
	return render(request, 'blog/lista.html', {'posts':posts})