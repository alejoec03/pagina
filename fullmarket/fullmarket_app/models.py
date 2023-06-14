from django.db import models

# Create your models here.

class Producto(models.Model):
	titulo = models.CharField(max_length=200)
	precio = models.PositiveIntegerField()
	descripcion = models.CharField(max_length=10000)
	pic = models.CharField(max_length=100)
	