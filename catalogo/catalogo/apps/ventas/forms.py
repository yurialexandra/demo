from catalogo.apps.ventas.models import Producto, Marca
from django import forms

class add_producto_form(forms.ModelForm):
	class Meta:
		model   = Producto
		# se excluye el status por que en el modelo lo ponemos defautl - true
		exclude = {'status',}

class agregar_marca_form(forms.ModelForm):
	class Meta:
		model   = Marca
		
