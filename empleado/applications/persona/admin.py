from django.contrib import admin
from .models import Empleado, Habilidades


#modificadores del admin de django
class EmpleadoAdmin(admin.ModelAdmin):
    #lista de campos a mostrar en el admin. . . 
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job','full_name'
    )
    #si quiero otro campo en el admin al lado de los anteriores ejemplo *full_name*
    # defino la funcion, traifo los campos los uno y la llamo arriba
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # este filtra por parametro o campo un buscador por primer nombre
    search_fields = ('first_name',)
    #lista para filtrar por trabajos 'job' a la derecha
    list_filter = ('job',)
    #filtro q permite agrgar muchas habilidades a un empleado cool
    filter_horizontal = ('habilidades',)

# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)