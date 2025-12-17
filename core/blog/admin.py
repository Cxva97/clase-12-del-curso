from django.contrib import admin
from .models import Categoria, Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'category']
    
    
@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']