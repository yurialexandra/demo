from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_producto_form
from catalogo.apps.ventas.models import Producto, Marca
from catalogo.apps.ventas.models import  Categoria
from django.core.mail import  EmailMultiAlternatives
from django.http import HttpResponseRedirect
from catalogo.apps.ventas.forms import agregar_marca_form

def add_producto_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_producto_form (request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() # GUARDA LA INFORMACION
			formulario.save_m2m() # GUARDA LAS RELACIONES
			info = "Guardado satisfatoriamente"
			return HttpResponseRedirect('/')
	else:
		formulario = add_producto_form()
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))

def agregar_marca_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = agregar_marca_form (request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() # GUARDA LA INFORMACION
			formulario.save_m2m() # GUARDA LAS RELACIONES
			info = "Guardado satisfatoriamente"
			return HttpResponseRedirect('/')
	else:
		formulario = agregar_marca_form()
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('ventas/agregar_marca.html', ctx,context_instance = RequestContext(request))

def edit_producto_view(request, id_prod):
	info = ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario=add_producto_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.status=True
			edit_prod.save()
			info = "Guardado Satisfatoriamente"
			return HttpResponseRedirect('/')
	else:
		formulario = add_producto_form(instance = prod)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/edit_producto.html', ctx, context_instance = RequestContext(request))

def del_product_view(request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/productos/')
	except:
		info = "Producto no se puede Eliminar"
		return HttpResponseRedirect('/productos/')


def Marca_view(request, id_marc):
	lista_marc = Producto.objects.filter(status = True)
	ctx = {'productos':lista_marc}
	return render_to_response ('ventas/Marca.html', ctx, context_instance =  RequestContext(request))
