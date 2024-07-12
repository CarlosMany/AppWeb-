# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main_view, name='main'),
#     # path('', views.login_view, name='login'),
#     path('login/', views.login_view, name='login'),
#     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
#     # Existing paths...
#     path('item/<int:pk>/', views.item_detail, name='item_detail'),
#     path('item/new/', views.item_new, name='item_new'),
#     path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
#     path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
#     path('items/', views.item_list, name='item_list'),
#     #codigo agregado
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    
    # URLs de Item
    path('items/', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/new/', views.item_new, name='item_new'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    
    # URLs de Cliente
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    
    # URLs de Contacto
    path('contactos/', views.contacto_list, name='contacto_list'),
    path('contacto/<int:pk>/', views.contacto_detail, name='contacto_detail'),
    path('contacto/new/', views.contacto_new, name='contacto_new'),
    path('contacto/<int:pk>/edit/', views.contacto_edit, name='contacto_edit'),
    path('contacto/<int:pk>/delete/', views.contacto_delete, name='contacto_delete'),
    
    # URLs de Empresa
    path('empresas/', views.empresa_list, name='empresa_list'),
    path('empresa/<int:pk>/', views.empresa_detail, name='empresa_detail'),
    path('empresa/new/', views.empresa_new, name='empresa_new'),
    path('empresa/<int:pk>/edit/', views.empresa_edit, name='empresa_edit'),
    path('empresa/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),
    
    # URLs de Producto
    path('productos/', views.producto_list, name='producto_list'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/new/', views.producto_new, name='producto_new'),
    path('producto/<int:pk>/edit/', views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
    
    # URLs de Venta
    path('ventas/', views.venta_list, name='venta_list'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new/', views.venta_new, name='venta_new'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
    path('venta/<int:pk>/delete/', views.venta_delete, name='venta_delete'),
    
    # URLs de Empleado
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleado/<int:pk>/', views.empleado_detail, name='empleado_detail'),
    path('empleado/new/', views.empleado_new, name='empleado_new'),
    path('empleado/<int:pk>/edit/', views.empleado_edit, name='empleado_edit'),
    path('empleado/<int:pk>/delete/', views.empleado_delete, name='empleado_delete'),
]
