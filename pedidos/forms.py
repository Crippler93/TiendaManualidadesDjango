from django import forms
from .models import Pedido

class FormCreaPedido(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = ['nombre', 'apellido', 'email', 'direccion']
		