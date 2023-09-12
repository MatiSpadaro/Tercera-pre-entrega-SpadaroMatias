from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Muito3D"
admin.site.register(Productos)
