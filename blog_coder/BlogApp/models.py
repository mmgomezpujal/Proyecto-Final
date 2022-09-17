from django.db import models

class Articulo(models.Model): 
    titulo = models.CharField(max_length=128)
    fecha = models.DateField()
    autor = models.CharField(max_length=128)
    email_autor = models.EmailField()

# Create your models here.
