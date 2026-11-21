# Sistema de Facturación en Python

Aplicación de escritorio para **gestionar clientes, productos y facturas**, con interfaz gráfica en **Tkinter** y almacenamiento en **MySQL**. Las facturas se exportan a archivos de texto.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-4B8BBE)
![MySQL](https://img.shields.io/badge/MySQL-Server-4479A1?logo=mysql&logoColor=white)

## Funcionalidades

- Interfaz gráfica con pestañas para **clientes**, **productos** y **facturas**.
- Alta, listado y selección de clientes y productos.
- Creación de facturas con múltiples ítems y cálculo del total.
- Exportación de cada factura a un archivo `factura_<id>.txt`.
- Persistencia de los datos en MySQL.

## Estructura

```
Facturacion-Python/
├── main.py        # Punto de entrada: inicia la interfaz gráfica
├── gui.py         # Interfaz con Tkinter (pestañas de clientes, productos y facturas)
├── database.py    # Conexión y consultas a MySQL
├── models.py      # Clases de cliente, producto y factura
└── utils.py       # Formateo de tablas (tabulate) y guardado de facturas a .txt
```

## Requisitos

- Python 3.x
- MySQL Server
- Paquetes de Python: `mysql-connector-python`, `tabulate`, `python-dateutil`

## Instalación

```bash
git clone https://github.com/KikeGonRam/Facturaci-nPython.git
cd Facturaci-nPython

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install mysql-connector-python tabulate python-dateutil
```

Crea la base de datos en MySQL:

```sql
CREATE DATABASE facturacion;
```

Y ajusta tus credenciales de conexión (host, usuario y contraseña) en `database.py`.

## Uso

Con el servidor MySQL en ejecución:

```bash
python main.py
```

## Tecnologías

Python · Tkinter · MySQL · tabulate

---

Proyecto de Luis Enrique González Ramírez — [github.com/KikeGonRam](https://github.com/KikeGonRam)
