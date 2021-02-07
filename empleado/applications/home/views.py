from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Prueba

#importo elformulario creado en forms.py
#para vincularlo a una vista
from .forms import PruebaForm

# Create your views aqui

class mitv(TemplateView):
    template_name = "home/hola.html"
    

class pruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    #campos q quiero traer edel modelo para crear el registro
    # fields = ('__all__')
    #normalmente se utliza el anterior linea
    #pero para indicar los fields con un formulario personalizado
    # de forms.py utilizo lo siguiqte fields...el formulario importado arriba
    form_class = PruebaForm
    success_url = '.'

