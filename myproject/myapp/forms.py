# from django import forms
# from .models import Item

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('name', 'Empresa', 'description')

from django import forms
from .models import Item, Cliente, Contacto, Empresa, Producto, Venta, Empleado

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'Empresa')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'email', 'telefono', 'direccion')

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'telefono', 'cliente')

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre', 'direccion', 'telefono', 'email', 'cliente')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio')

class VentaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    class Meta:
        model = Venta
        fields = ('fecha', 'cantidad', 'cliente', 'producto')
        

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'puesto', 'email', 'telefono')