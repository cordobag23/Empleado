from django.contrib import admin
from django.urls import path
from .import views

#esto permite ubicar las urls y ya con el name ubicamos la especifica para el reverse_laz
# q es el q redirecciona
#            nombre de la aplicacion, departamneto guion bajo app
app_name = 'departamento_app' 

urlpatterns = [
    path('newdepapersona/', views.NewDEparEmplead.as_view(), name='depaempleado'),
    path('listaDepartame/', views.DepartamentoListView.as_view(), name='listdepa'),
    
   

]








