from distutils.command.upload import upload
from django.db import models

class Articulo(models.Model): 
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=128, null=True, blank=True)
    fecha = models.DateField()
    autor = models.CharField(max_length=128)
    email_autor = models.EmailField()
    cuerpo = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

# Create your models here.
