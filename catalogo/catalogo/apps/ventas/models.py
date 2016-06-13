from django.db import models


class Categoria (models.Model):
	nombre      = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 500)


	def __unicode__(self):
		return self.nombre

class Marca (models.Model):
	nombre      = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombre

class Producto (models.Model):
		
	def url (self, filename):
		ruta ="MultimediaData/producto/%s/%s"%(self.nombre, str(filename))
		return ruta


	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=500)
	status      = models.BooleanField(default=True)
	imagen      = models.ImageField(upload_to=url, null=True,blank=True)
	precio      = models.DecimalField(max_digits=10,decimal_places=2)
	stock       = models.IntegerField()
	categorias  = models.ManyToManyField(Categoria, null = True, blank = True)
	marca       = models.ForeignKey(Marca)

	def __unicode__ (self):
		return self.nombre


