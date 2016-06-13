from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'catalogo.views.home', name='home'),
   
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalogo.apps.home.urls')),
    url(r'^',include('catalogo.apps.ventas.urls')),
    url(r'^',include('catalogo.apps.webservices.ws_productos.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
 

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:



)
