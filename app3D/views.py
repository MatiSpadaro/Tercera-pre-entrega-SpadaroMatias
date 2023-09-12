from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")

def productos(req):
    return render(req, "productos.html")

def pedidos(req):
    return render(req, "pedidos.html")

def pedidos(request):
    if request.method == "POST":
        pedido=Pedidos(modelo3D=request.POST["modelo3D"], material=request.POST["material"])
        pedido.save()
        return render(request,"inicio.html")
    else:
        return render(request, "pedidos.html")