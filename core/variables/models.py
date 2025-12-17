from django.db import models

# Create your models here.
class Student (models.Model):
    gender_choices = [
        ('M', 'masculino'),
        ('F', 'femenino'),
        ('O', 'otro'),
    ]
    
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=1,
        choices= gender_choices,
        blank=True
    )
    birthday =models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.lastName}"