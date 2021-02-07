from django.contrib import admin
from django.urls import path
from .import views

#esto permite ubicar las urls y ya con el name ubicamos la especifica para el reverse_laz
# q es el q redirecciona
#            nombre de la aplicacion, persona guion bajo app
app_name = 'persona_app'

urlpatterns = [
    path('listaempleados/', views.ListaAllEmpleadosListView.as_view(), name='empleados_all'),
     # <shortname>/ es el valor q mando en la url y lo recoje el kwor en la vista
    path('lista-by-area/<shortname>/', views.ListByAreaEmpleadoListView.as_view(), name='empleados_area'),
    path('buscar-empleado/', views.ListEmpleadoPalabraCLaveListView.as_view()),
    path('habilidades-empleado/', views.ListaHabilidadesEmpleaListView.as_view()),
    # para identificar de quien quiero ver los detalles utilizo <pk>
    path('detalle-empleado/<pk>/', views.DetailEmpleadoDetailView.as_view(), name='empleado_detail'),
    path('succes/', views.successdx.as_view(), name='correcto'),
    path('add/', views.EmpleadoCreateView.as_view(), name='add'),
    # para modificar u empleado le mandamos pòr la url a traves el <pk> que quiero editar 
    path('updateempleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificarempleado'),
     # para eliminar un empleado le mandamos pòr la url a traves el <pk> que quiero eliminar 
    path('deleteempleado/<pk>/', views.EnpleadoDeleteView.as_view(), name='eliminarempleado'),
    path('listarempleadmin/', views.ListAdminEmpleados.as_view(), name='list_admin'),

    path('', views.InicioView.as_view()),

]
