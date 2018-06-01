from django.db import models

class InfoBasica(models.Model):
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	direccion = models.TextField()

	def __str__(self):
		return self.nombres

class InfoAdicional(models.Model):
	nomb = models.ForeignKey(InfoBasica, null=True, related_name='adicional',on_delete=models.CASCADE)
	arte = models.CharField(max_length=100)
	cine = models.CharField(max_length=100)
	musica = models.CharField(max_length=100)

#	def __str__(self):
#		return str(self.nomb)