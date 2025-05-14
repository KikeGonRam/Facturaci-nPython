Sistema de Facturación en Python
Este es un sistema de facturación simple desarrollado en Python. Permite gestionar clientes, productos y facturas, almacenando la información en una base de datos SQLite y generando facturas en archivos de texto.
Requisitos

Python 3.x
Módulos: tabulate, python-dateutil

Instalación

Clona o descarga el proyecto.
Crea un entorno virtual:python -m venv venv


Activa el entorno virtual:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate


Instala las dependencias:pip install tabulate python-dateutil


Ejecuta el programa:python main.py



Funcionalidades

Agregar clientes y productos.
Crear facturas con múltiples productos.
Listar clientes, productos y facturas.
Guardar facturas en archivos de texto.

Estructura del Proyecto

main.py: Menú principal y lógica de interacción.
database.py: Manejo de la base de datos SQLite.
models.py: Clases para clientes, productos y facturas.
utils.py: Funciones auxiliares para formateo y guardado.
facturacion.db: Base de datos SQLite (se crea automáticamente).

