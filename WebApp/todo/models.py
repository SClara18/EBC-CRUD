from django.db import models

# Create your models here.
class Tarea(models.Model):
	tarea = models.CharField(max_length=100)
	maestro = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.tarea
		return self.maestro
		return self.descripcion
