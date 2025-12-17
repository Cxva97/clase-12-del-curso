from django.contrib import admin
from .models import Cursos, Listado, Profesor, PerfilProfesor
# Register your models here.
admin.site.register(Cursos)
admin.site.register(Listado)
admin.site.register(Profesor)
admin.site.register(PerfilProfesor)