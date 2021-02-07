from django.shortcuts import render
from django.urls import reverse_lazy
#importo el formulario 
from .forms import NewDEpartamentoForm 
#importo la vista q funciona con mas de un modelo
from django.views.generic.edit import FormView
from django.views.generic import ListView
#importo el modelo Empleado para utilizarlo en el form_valid con el cleaned_data
from applications.persona.models import Empleado
#importo el modelo departamento para utilizarlo en el form_valid con el cleaned_data
from .models import Departamento

#creo la clase 
class NewDEparEmplead(FormView):
    template_name = 'departamento/newdepartameempleado.html'
    #como vamos a recibir datos, necesitamos un formulario 
    #para q reciba esos datos, el creadoe n forms.py, lo importo
    form_class = NewDEpartamentoForm
    #pagina q indica q se realixo satisfactoriament
    success_url = '/'

    #SOBREESCRIBIMOS LA SIGUIETE FUNCION
    def form_valid(self, form):
        #necesita q se retorne con el super, y le nadamos el nombre se la clase
        print('-*******estamaos en el forrmmm validdd*********')
        #aqui recuppero la info q envio de los fortmularios, d cada campo
        # utilizando el form q me llega como parametro
        # y su atributi y diccionario,  cleaned_data['nombre], nombre d cada uno d 
        #los campos q vienen desde los campos del form
        nombrex = form.cleaned_data['nombre']
        apellidox = form.cleaned_data['apellidos']

        #CREANDO O Instanciando DEPARTAMENTO, se puede crear d cualquiera
        # de las dos maneras, esta o la de abajo empleado
        # en este caso creo el objeto depa, y lleno los valores del mdelo directamente
        # recogiendo los datos del formulario
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname'],
        )
        # lo guardo en la base de datos
        depa.save()


        #CREANDO EMPLEADO
        #comienzo a registrar un empleado, utilizo objects (filtrar, recuoperar o REGISTRAR)
        #es algo asicomo crear un objeto, instanciarlo, EMpleado, todo con el create
        Empleado.objects.create(
            # a los campos del modelo le mando los valores de arriba
            first_name = nombrex,
            last_name = apellidox,
            job = '1',
            #como es una llave foranea, debo instanciar o crear un modelo
            #DEPARTAMENTO arriba para ppoder utilizarlo
            departamento = depa


        )
        return super(NewDEparEmplead, self).form_valid(form)


# listar DEPARTAMENTOS
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'depas'