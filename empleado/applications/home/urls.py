from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('mitv/', views.mitv.as_view()),
    path('add-prueba/', views.pruebaCreateView.as_view()),
    
]
