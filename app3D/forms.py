from django import forms

class PedidosFormulario(forms.Form):
    
    modelo3D= forms.CharField(max_length=40)
    material= forms.CharField(max_length=40)

class ProductosFormulario(forms.Form):
    
    claseProducto = forms.CharField(max_length=40)
    nombreProducto = forms.CharField(max_length=40)
    