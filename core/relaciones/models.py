
from django.db import models
from django.conf import settings
from variables.models import Student
# Create your models here.
#many to one - muchos a uno
class Cursos(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    
class Listado(models.Model):
    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='listado')
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name='listado')
    
#muchos a muchos
class Profesor(models.Model):
    name = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Cursos, related_name='profesores')
    
# uno a uno
class PerfilProfesor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    numero = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
