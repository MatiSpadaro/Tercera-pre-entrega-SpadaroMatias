from django.contrib import admin
from .models import *
# Register your models here.

class productosAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto',)
    
    search_fields=('nombreProducto',)

admin.site.site_header = "Muito3D"
admin.site.register(Productos, productosAdmin)
