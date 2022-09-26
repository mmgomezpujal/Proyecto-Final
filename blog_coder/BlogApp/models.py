from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField

class Articulo(models.Model): 
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=128, null=True, blank=True)
    fecha = models.DateField()
    autor = models.CharField(max_length=128)
    email_autor = models.EmailField()
    cuerpo = RichTextField(blank=True, null= True)
    # imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo}'


# Create your models here.
