from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    short_name = models.CharField('Nombre corto', max_length=50, unique=True)
    anulate = models.BooleanField('anulado', default=False)


    class Meta:
        verbose_name = 'Mi Departamaento'
        verbose_name_plural = 'Areas de la empresa'

    
    def __str__(self):
        return self.name

