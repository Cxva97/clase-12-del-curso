from django.db import models

# Create your models here.
class Producto(models.Model): #Crea la plantilla de db en base a los modelos de django
    nombre= models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad =models.IntegerField()
    disponible =models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    etiqueta = models.CharField(max_length=50)
    contenido = models.TextField()
    
    def __str__ (self):
        return f"{self.titulo}"