Sistema de Facturación en Python con Interfaz Gráfica y MySQL
Este es un sistema de facturación mejorado desarrollado en Python con una interfaz gráfica usando tkinter y una base de datos MySQL. Permite gestionar clientes, productos y facturas, almacenando la información en MySQL y generando facturas en archivos de texto.
Requisitos

Python 3.x
MySQL Server
Módulos: mysql-connector-python, tabulate, python-dateutil

Instalación

Clona o descarga el proyecto.
Configura una base de datos MySQL:CREATE DATABASE facturacion;


Crea un entorno virtual:python -m venv venv


Activa el entorno virtual:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate


Instala las dependencias:pip install mysql-connector-python tabulate python-dateutil


Actualiza las credenciales de MySQL en database.py (host, user, password).
Ejecuta el programa:python main.py



Funcionalidades

Interfaz gráfica con pestañas para gestionar clientes, productos y facturas.
Agregar, listar y seleccionar clientes y productos.
Crear facturas con múltiples ítems.
Guardar facturas en archivos de texto.
Almacenamiento de datos en MySQL.

Estructura del Proyecto

main.py: Inicia la aplicación gráfica.
database.py: Manejo de la base de datos MySQL.
models.py: Clases para clientes, productos y facturas.
utils.py: Funciones auxiliares para formateo y guardado.
gui.py: Implementación de la interfaz gráfica con tkinter.

Notas

Asegúrate de que el servidor MySQL esté en ejecución antes de iniciar la aplicación.
Las facturas se guardan como archivos de texto en la carpeta del proyecto.

