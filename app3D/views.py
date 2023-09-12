from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")

def productos(req):
    return render(req, "productos.html")