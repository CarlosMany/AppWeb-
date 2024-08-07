# AppWeb //

## Proyecto Desarrollo Web 2

Esta aplicación es un CRUD orientado a CRM básico, la finalidad es ir mejorándolo cada vez más para ser un completo CRM.

## Manual de Usuario


#### a. Acceso a la aplicación

1. Abre tu navegador web.
2. Ingresa la URL de la aplicación en la barra de direcciones.
3. En la página de inicio, ingresa tu nombre de usuario y contraseña.
4. Haz clic en el botón **Login**.
5. Serás redirigido a tu tablero de usuario o al tablero de administrador según tu rol.

#### b. Alta de documentos

1. Al ingresar se mostrará el tablero principal.
2. Haz clic en el botón **Nuevo Cliente (o seleccionar el tipo que se quiere dar de alta)**.
3. Completa los campos requeridos en el formulario de creación de registro.
4. Haz clic en el botón **Guardar** para almacenar el nuevo registro en la base de datos.

#### c. Edición de documentos

1. Navega al menú **Cliente (o el tipo correspondiente)** en el tablero principal.
2. Identifica el registro que deseas editar de la lista de registros.
3. Haz clic en el botón **Editar** junto al resgistro.
4. Realiza los cambios necesarios en el formulario de edición.
5. Haz clic en el botón **Guardar** para actualizar el registro.

#### d. Baja de documentos

1. Navega al menú **Cliente (o el tipo correspondiente)** en el tablero principal..
2. Identifica el registro que deseas eliminar de la lista de registros.
3. Haz clic en el botón **Eliminar** junto al registro seleccionado.


#### e. Consulta de documentos

1. Navega al menú **Cliente (o el tipo correspondiente)** en el tablero principal.
2. Te apareceran los detalles y registros que se han realizado.
## Descargar y Usar el Proyecto

### Requisitos Previos

- Python 3.x
- Django

### Instrucciones

1. Clona el repositorio: git clone https://github.com/CarlosMany/AppWeb-.git
2. Navega al directorio del proyecto: cd AppWeb/myproject
3. Instala las dependencias: pip install -r requirements.txt
4. Realiza las migraciones de la base de datos: python manage.py migrate
5. Crea un superusuario para acceder al panel de administración: python manage.py createsuperuser
6. Inicia el servidor de desarrollo: python manage.py runserver
7. Abre tu navegador web y navega a http://127.0.0.1:8000/admin para acceder al panel de administración.

## Versión

### Versión 1

Esta es la versión 1 de la aplicación, en la cual solo se desarrolló el panel de administrador.

### Versión 2 (Planeada)

Para la versión 2, se tiene planeado desarrollar el panel de usuario, el cual permitirá:
- Ver sus compras.
- Realizar pedidos.
- Ver el estatus de sus pedidos/compras.

## Licencia

Este proyecto está licenciado bajo la Licencia GPL-3.0. Para más detalles, consulta el archivo `LICENSE`.
