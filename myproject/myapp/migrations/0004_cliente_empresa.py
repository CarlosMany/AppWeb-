# Generated by Django 5.0.6 on 2024-07-12 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cliente_empleado_producto_contacto_empresa_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Empresa',
            field=models.ForeignKey(default='Sin empresa', on_delete=django.db.models.deletion.CASCADE, to='myapp.item'),
        ),
    ]
