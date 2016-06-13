
from  django.conf.urls.defaults import  patterns, url,include

urlpatterns = patterns('catalogo.apps.ventas.views',
 	url(r'^add/producto/$','add_producto_view',name = 'vista_agregar_producto'),
    url(r'^edit/producto/(?P<id_prod>.*)/$', 'edit_producto_view', name = 'vista_editar_producto'),
    url(r'^del/producto/(?P<id_prod>.*)/$', 'del_product_view', name = 'vista_eliminar_producto'),
    url(r'^marca/(?P<id_marc>.*)/$', 'Marca_view', name = 'vista_marca_producto'),
    url(r'^agregar/marca/$','agregar_marca_view',name = 'vista_agregar_marca'),


)
