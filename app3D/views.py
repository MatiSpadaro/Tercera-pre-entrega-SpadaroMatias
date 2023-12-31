from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import PedidosFormulario, ProductosFormulario

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")

def productos(req):
    producto = Productos.objects.all()
    return render(req, "productos.html",{'productos':producto})

def agregarProductos(request):
       
    if request.method == "POST":
        
        miFormulario1 = ProductosFormulario(request.POST)
        
        if miFormulario1.is_valid():
            
            data = miFormulario1.cleaned_data
            
            producto=Productos(claseProducto=data["claseProducto"],nombreProducto=data["nombreProducto"])
            producto.save()
            return render(request,"Inicio.html")
    else:
        miFormulario1 = ProductosFormulario()
        return render(request,"agregarProductos.html",{"miFormulario1": miFormulario1})
    
def pedidos(request):
    
    if request.method == "POST":
        
        miFormulario = PedidosFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            pedido=Pedidos(modelo3D=data["modelo3D"],material=data["material"])
            pedido.save()
            return render(request,"Inicio.html")
    else:
        miFormulario = PedidosFormulario()
        return render(request,"pedidos.html",{"miFormulario": miFormulario})
    
def busquedaProductos(request):
    return render(request, "busquedaProductos.html")

def buscar(request: HttpRequest ):
    try:
        if request.GET["nombreProducto"]:
            nombreProducto=request.GET["nombreProducto"]
            producto = Productos.objects.filter(nombreProducto__icontains=nombreProducto)
            return render(request,"resultadoBusqueda.html", {"nombreProducto":producto})
    except:
            return HttpResponse(f"No hay producto con ese nombre.")
    
