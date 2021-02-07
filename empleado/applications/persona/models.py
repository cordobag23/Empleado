from django.db import models
from applications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    
    def __str__(self):
        return self.habilidad



class Empleado(models.Model):

    JOB_CHOICES = (
        ('0','Ingenier'),
        ('1','Administrador'),
        ('2','Contador'),
        ('3','Otro'),

    )
        

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField(max_length=50, choices = JOB_CHOICES)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    #relacion de uno a muchos, un empleado puede perteneces a un solo departamento, y un
    # departamento puede estar en varios empleados
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #relacion de muchos a muchos= una habilidad le puede pertenecer a varios empleados y un empleado
    # puede tener muchas habilidades
    habilidades = models.ManyToManyField(Habilidades, blank=True)

    def __str__(self):
        return self.first_name

