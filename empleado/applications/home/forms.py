"""comienzo a prersonalizar mi form q viene por defecto
para ello creo un archivo forms.py en cada una de mis apps
en este archivo, escribo la personalizacion para
los campos del modelo """
#importo paquete
from django import forms
from .models import Prueba
#se escribira codigo en python que haga que:
# se conecten los campos del modelo mediante
# un formulario forms.py conla vista
# es dceir q se conecten los campos del modelo con
# la vista para que se pinte en el html
#mediante el forms.py

#inicio del formulario
class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        # q atributos del modelo quieo convertirlo
        #en el formulario para q se muestre en el html
        fields = ('__all__')
        #AHORA IMPORTO EN LAs VISTAs, ESTE FORMULARIO CREADO 
        #para vincularlo a una vista

        #para perosnalizar mi formulario con los WIDGETS:
        widgets = {
            #ingreso los campos a personalizar del modelo
            #otra vez utilizo forms q es la q hereda d todo
            'name':forms.TextInput(
                #aca los atributos q quiero agregarñle en otro diccionario
                attrs ={
                    'placeholder':'Ingrese su nombre aqui',
                }
            )
        }




        #para validar uino de los campos del modelo prueba
        # defino una funcion clean_micampoavalidar(self)
    def clean_name(self):
            #recupero el valor de mi variable name
            # con cleaned_data['micampovalidar']
        name = self.cleaned_data['name']
            #creo la logica
        if name == 'looo':
                #funcion raise q pinta un error en el html con el ValidationError
            raise forms.ValidationError('ese nombre solo es d luisa')
        return name

# fin del formulario