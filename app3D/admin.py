from django.contrib import admin
from .models import *

# Register your models here.

class productosAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto',"claseProducto",)
    
    search_fields=('nombreProducto', "claseProducto")
    
    list_filter= ('nombreProducto', "claseProducto")

class pedidosAdmin(admin.ModelAdmin):
    list_display = ('modelo3D',"material",)
    
    search_fields=('modelo3D',"material",)
    
    list_filter= ('modelo3D',"material",)
    
admin.site.site_header = "Muito3D"
admin.site.register(Productos, productosAdmin)
admin.site.register(Pedidos,pedidosAdmin)
