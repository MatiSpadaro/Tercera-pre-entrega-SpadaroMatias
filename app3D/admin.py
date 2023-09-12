from django.contrib import admin
from .models import *

# Register your models here.

class productosAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto',"claseProducto",)
    
    
    
    search_fields=('nombreProducto', "claseProducto")
    
    list_filter= ('nombreProducto', "claseProducto")
   
    
admin.site.site_header = "Muito3D"
admin.site.register(Productos, productosAdmin)
