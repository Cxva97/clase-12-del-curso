from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"
    
class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='post'
    )