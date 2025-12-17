from django.contrib import admin
from .models import Producto, Post

# Register your models here.
admin.site.register(Producto)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'etiqueta', 'contenido']
    list_filter =['titulo']
    search_fields = ['titulo', 'contenido']
    ordering=['-titulo']
    list_per_page = 2
    