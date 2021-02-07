from django.db import models

# Create your models here.
class Prueba(models.Model):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    
    def __str__(self):
        return self.name
