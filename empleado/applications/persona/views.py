from django.shortcuts import render
#para rediireccionar una pagina, utiliza el name de una url
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, 
    TemplateView, UpdateView, DeleteView   
)
#modelos
from .models import Empleado
from applications.departamento.models import Departamento
# vista para la pagina de inicio

class InicioView(TemplateView):
    template_name = 'inicio.html'

#listar todos los empleados
class ListaAllEmpleadosListView(ListView):
    template_name = "persona/list_all.html"
    #al crear el paginate_by, internamente se crea la variable is_paginated
    #q se utiliza para paginar y maniular similares
    paginate_by = 2
    ordering = 'first_name'

  #una vartiable es bucar empleados por nombre
    def get_queryset(self):
         #BAMOS A RECOJER EL VALOR con id y name kword de la caja del html
         # es decir todas las solicitudes q se envian desde el html a traves del get
         # solicitud en ingles es request
         # es decir, guardo en palabra_clave = las solitudes de tipo GET con id = kword
         # y como es una tupla se coloca la , y el ''

         palabra_clave = self.request.GET.get('kword', '')
         if palabra_clave:
             #para un mejor fiñltrado solo con un oar de letras
             #utilizo el icontains, en npmbre del atruibuto a filtrar
             # doble guin bajo icontains ,,,, antes: lista = Empleado.objects.filter(first_name=palabra_clave)
             #                      despues: 
            lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
            
         else: 
            lista = Empleado.objects.all()
         return lista
    
#lista empleads por area
class ListByAreaEmpleadoListView(ListView):
    model = Empleado
    template_name = "persona/list_by_area.html"

    def get_queryset(self):
        # recojo el valor <shortname> q indique en la url y lo guard en area
        # con el metodo kwargs, co ese recojo lo q me manda por url
        area = self.kwargs['shortname']
        # expli, como el departamento es un modelo aparte, y una relacion 1 a muchos
        # para llamar un campo de ese modelo departamento, solo escribio el nombre del
        # modelo seguido de dos guines bajos seguido de el campo q quiero traer
        lista = Empleado.objects.filter(departamento__short_name = area)
        return lista
 
class ListEmpleadoPalabraCLaveListView(ListView):
     model = Empleado
     template_name = "persona/by_kword.html"
     context_object_name = 'empleados'

     def get_queryset(self):
         #BAMOS A RECOJER EL VALOR con id y name kword de la caja del html
         # es decir todas las solicitudes q se envian desde el html a traves del get
         # solicitud en ingles es request
         # es decir, guardo en palabra_clave = las solitudes de tipo GET con id = kword
         # y como es una tupla se coloca la , y el ''
         palabra_clave = self.request.GET.get('kword', '')
         lista = Empleado.objects.filter(first_name=palabra_clave)
         print('lista resultadoss ******** ', lista)
         return lista
 
#listar habilidades de un empleado... MUCHOS A MUCHOS, un empleado tiene m uchas habilidades
# una habilidad puede pertenecer a muchos empleados
# este trae una kista de habilidades solo de UN EMPLEADO A LA VEZ

class ListaHabilidadesEmpleaListView(ListView):
    model = Empleado
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        # como solo quiero el regitro de UN SOLO EMPLEADO
        # utilizo el get en ves del filter, con el id lo filtramos pk
        #traigo el empleado con el id indicado
        empleado = Empleado.objects.get(pk=4)
        #ya tengo el empleado, ahora traigo todas sus habilidades
        return empleado.habilidades.all()

# detalles de los registros etc
#esta vista ya busca automaticamnete el empleado, lo unico es ponerle un <pk>
#en la url y ya desde el navegador le indicamo la pk deseada mipagina/1 

class DetailEmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

# pagina succes o proceso exitoso
class successdx(TemplateView):
    template_name = "persona/succes.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #le indico los campos q quiero llamar en el formulario
    # si quiero algunos solo  fields = ['first_name', 'last_name']
    # si quiero todos los campos solo coloco fields = ('__all__')  doble guin bajo
    #para enviar estos campos y  registrar utilizo el post con el form en el template
    fields = ('__all__')
    #necesita el campo ursucces para indicar a dond quiere ir cuando la carga de datos este complesta
    #le indico q se dirija a la misma template.... si quieor a otra temaplate, creo la vista, la url y ya aca la ahgrgo
    #success_url = '/succes'
    #UNA MEJOR MANERA DE REDIRECCIONAR ES CON reverse_lazy, q recibe el name de una url
    success_url = reverse_lazy('persona_app:add')

#ETIDAR TREGISTROS UPDATEVIEW

class EmpleadoUpdateView(UpdateView):
    #como saber a q regfistro apunta el updatoview
    # en este caso es el pk que lo pasamos como parametro en la url <pk> 
    model = Empleado
    template_name = "persona/update.html"
    # le mando los fields q quiero actualizar, y los cargo con un form en la template
    fields = ('__all__')
    #una redireccion al hacer efectivo el cambio
    success_url = reverse_lazy('persona_app:list_admin')
    

#eliminar registros
#siempre va a preguntar si dese elimir el rigistro q en este caso le mando por url con el pk
#esto sd pregunta en la template y se confirm con un boton
# no olvidar q al mandar info o eliminar rgistro se manda por post

class EnpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    #al copletar el eliminado se va a esta pagina
    success_url = reverse_lazy('persona_app:list_admin')
    context_object_name = 'eliminarempleado'
    


#LISTAR EMPLEADOS PARA EL ADMIN (EDITAR, EÑLIMINAR)
class ListAdminEmpleados(ListView):
    template_name = "persona/list_admin_empleados.html"
    paginate_by = 2
    ordering = 'first_name'

  #una vartiable es bucar empleados por nombre
    def get_queryset(self):
         palabra_clave = self.request.GET.get('kword', '')
         if palabra_clave:    
            lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
            
         else: 
            lista = Empleado.objects.all()

         return lista


        



    
