from django.contrib import admin
from django.urls import path
from app3D.views import *

urlpatterns = [
   
    path('inicio/', inicio, name ="Inicio"),
    path('productos/', productos , name="Productos"),
    path('agregarProductos/', agregarProductos , name="agregarProductos"),
    path('pedidos/', pedidos , name="Pedidos"),
    path('busquedaProductos/', busquedaProductos, name="busquedaProductos"),
    path('buscar/', buscar , name="buscar"),
]
