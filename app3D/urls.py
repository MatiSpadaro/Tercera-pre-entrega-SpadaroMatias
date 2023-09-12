from django.contrib import admin
from django.urls import path
from app3D.views import *

urlpatterns = [
   
    path('inicio/', inicio, name ="Inicio"),
    path('productos/', productos , name="Productos"),
    
]
