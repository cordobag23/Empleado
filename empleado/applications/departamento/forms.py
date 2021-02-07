# SE NECESITA REGISTRAR UN DEPARTAMENTO Y A LA VEZ
# REGISTRAR UN EMPLEADO, PERO un modelo permite registrar
# un solo modeo a la vez, u depa o un empleadfp
#para ello utilizamos un FORMULARIO SIMPLE
#este no esta asociado a mningun modelo en especifico
# saco los datos de un modelo y de otr5o y lo plasmp
# en un nuevo formmualrio

#importo el formulario
from django import forms

#creo el formulario en base a una clase

class NewDEpartamentoForm(forms.Form):
    #en cada variable guardo el contenido de los 
    # campos de cada modelo, 
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=50)
