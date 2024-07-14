from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Cliente, Contacto, Empresa, Producto, Venta, Empleado
from .forms import ItemForm, ClienteForm, ContactoForm, EmpresaForm, ProductoForm, VentaForm, EmpleadoForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Vistas de Item
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')

# Vistas de Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente_detail.html', {'cliente': cliente})

# def cliente_new(request):
#     if request.method == "POST":
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             cliente = form.save(commit=False)
#             cliente.save()
#             return redirect('cliente_detail', pk=cliente.pk)
#     else:
#         form = ClienteForm()
#     return render(request, 'cliente_form.html', {'form': form})
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Redirigir a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

# def cliente_edit(request, pk):
#     cliente = get_object_or_404(Cliente, pk=pk)
#     if request.method == "POST":
#         form = ClienteForm(request.POST, instance=cliente)
#         if form.is_valid():
#             form.save()
#             return redirect('cliente_detail', pk=cliente.pk)
#     else:
#         form = ClienteForm(instance=cliente)
#     return render(request, 'cliente_form.html', {'form': form})
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Redirigir a la lista de clientes
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente_list')

# Vistas de Contacto
def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto_list.html', {'contactos': contactos})

def contacto_detail(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contacto_detail.html', {'contacto': contacto})

# def contacto_new(request):
#     if request.method == "POST":
#         form = ContactoForm(request.POST)
#         if form.is_valid():
#             contacto = form.save(commit=False)
#             contacto.save()
#             return redirect('contacto_detail', pk=contacto.pk)
#     else:
#         form = ContactoForm()
#     return render(request, 'contacto_form.html', {'form': form})
def contacto_new(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_list')  # Redirigir a la lista de contactos
    else:
        form = ContactoForm()
    return render(request, 'contacto_form.html', {'form': form})

# def contacto_edit(request, pk):
#     contacto = get_object_or_404(Contacto, pk=pk)
#     if request.method == "POST":
#         form = ContactoForm(request.POST, instance=contacto)
#         if form.is_valid():
#             form.save()
#             return redirect('contacto_detail', pk=contacto.pk)
#     else:
#         form = ContactoForm(instance=contacto)
#     return render(request, 'contacto_form.html', {'form': form})
def contacto_edit(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_list')  # Redirigir a la lista de contactos
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contacto_form.html', {'form': form})

def contacto_delete(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_list')

# Vistas de Empresa
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa_list.html', {'empresas': empresas})

def empresa_detail(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'empresa_detail.html', {'empresa': empresa})

# def empresa_new(request):
#     if request.method == "POST":
#         form = EmpresaForm(request.POST)
#         if form.is_valid():
#             empresa = form.save(commit=False)
#             empresa.save()
#             return redirect('empresa_detail', pk=empresa.pk)
#     else:
#         form = EmpresaForm()
#     return render(request, 'empresa_form.html', {'form': form})
def empresa_new(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')  # Redirigir a la lista de empresas
    else:
        form = EmpresaForm()
    return render(request, 'empresa_form.html', {'form': form})

# def empresa_edit(request, pk):
#     empresa = get_object_or_404(Empresa, pk=pk)
#     if request.method == "POST":
#         form = EmpresaForm(request.POST, instance=empresa)
#         if form.is_valid():
#             form.save()
#             return redirect('empresa_detail', pk=empresa.pk)
#     else:
#         form = EmpresaForm(instance=empresa)
#     return render(request, 'empresa_form.html', {'form': form})
def empresa_edit(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')  # Redirigir a la lista de empresas
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa_form.html', {'form': form})

def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    empresa.delete()
    return redirect('empresa_list')

# Vistas de Producto
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})

# def producto_new(request):
#     if request.method == "POST":
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             producto = form.save(commit=False)
#             producto.save()
#             return redirect('producto_detail', pk=producto.pk)
#     else:
#         form = ProductoForm()
#     return render(request, 'producto_form.html', {'form': form})
def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')  # Redirigir a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

# def producto_edit(request, pk):
#     producto = get_object_or_404(Producto, pk=pk)
#     if request.method == "POST":
#         form = ProductoForm(request.POST, instance=producto)
#         if form.is_valid():
#             form.save()
#             return redirect('producto_detail', pk=producto.pk)
#     else:
#         form = ProductoForm(instance=producto)
#     return render(request, 'producto_form.html', {'form': form})
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')  # Redirigir a la lista de productos
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('producto_list')

# Vistas de Venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta_list.html', {'ventas': ventas})

def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'venta_detail.html', {'venta': venta})

# def venta_new(request):
#     if request.method == "POST":
#         form = VentaForm(request.POST)
#         if form.is_valid():
#             venta = form.save(commit=False)
#             venta.total = venta.producto.precio * venta.cantidad
#             venta.save()
#             return redirect('venta_detail', pk=venta.pk)
#     else:
#         form = VentaForm()
#     return render(request, 'venta_form.html', {'form': form})
def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad
            venta.save()
            return redirect('venta_list')  # Redirigir a la lista de ventas
    else:
        form = VentaForm()
    return render(request, 'venta_form.html', {'form': form})

# def venta_edit(request, pk):
#     venta = get_object_or_404(Venta, pk=pk)
#     if request.method == "POST":
#         form = VentaForm(request.POST, instance=venta)
#         if form.is_valid():
#             venta = form.save(commit=False)
#             venta.fecha = form.cleaned_data['fecha']
#             venta.total = venta.producto.precio * venta.cantidad
#             venta.save()
#             return redirect('venta_detail', pk=venta.pk)
#     else:
#         form = VentaForm(instance=venta)
#     return render(request, 'venta_form.html', {'form': form})
def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad
            venta.save()
            return redirect('venta_list')  # Redirigir a la lista de ventas
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    venta.delete()
    return redirect('venta_list')

# Vistas de Empleado
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleados': empleados})

def empleado_detail(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'empleado_detail.html', {'empleado': empleado})

def empleado_new(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('empleado_detail', pk=empleado.pk)
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})

def empleado_edit(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('empleado_detail', pk=empleado.pk)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado_form.html', {'form': form})

def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    return redirect('empleado_list')

# Otras vistas
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login.html')

# Login usuario
def login_view_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('user_dashboard')
            else:
                return redirect('admin_dashboard')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login_user.html')

def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    items = Item.objects.all()
    return render(request, 'admin_dashboard.html', {'items': items})

def user_dashboard(request):
    if not request.user.is_authenticated or request.user.is_staff:
        return redirect('login')
    return render(request, 'user_dashboard.html', {'user': request.user})

def main_view(request):
    return render(request, 'main.html')