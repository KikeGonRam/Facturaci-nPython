# Sistema de Facturación en Python

Aplicación de escritorio para **gestionar clientes, productos y facturas**, con interfaz gráfica en **Tkinter** y almacenamiento en **MySQL**. Cada factura se exporta a un archivo de texto.

[![Seguridad](https://github.com/KikeGonRam/Facturaci-nPython/actions/workflows/security.yml/badge.svg)](https://github.com/KikeGonRam/Facturaci-nPython/actions/workflows/security.yml)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Server-4479A1?logo=mysql&logoColor=white)

[Seguridad](SECURITY.md)

## Funcionalidades

| Módulo | Qué hace |
| --- | --- |
| Clientes | Alta, listado y selección. |
| Productos | Alta, listado y selección. |
| Facturas | Creación con múltiples ítems, cálculo del total y exportación a `factura_<id>.txt`. |
| Datos | Persistencia en MySQL. |

## Estructura

```
Facturacion-Python/
├── main.py       # Punto de entrada: inicia la interfaz gráfica
├── gui.py        # Interfaz con Tkinter (pestañas de clientes, productos y facturas)
├── database.py   # Conexión y consultas a MySQL
├── models.py     # Clases de cliente, producto y factura
└── utils.py      # Formateo de tablas (tabulate) y guardado a .txt
```

## Requisitos

- Python 3.x
- MySQL Server
- Paquetes: `mysql-connector-python`, `tabulate`, `python-dateutil`

## Instalación

```bash
git clone https://github.com/KikeGonRam/Facturaci-nPython.git
cd Facturaci-nPython
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install mysql-connector-python tabulate python-dateutil
```

Crea la base de datos y ajusta las credenciales de conexión en `database.py`:

```sql
CREATE DATABASE facturacion;
```

## Uso

Con el servidor MySQL en ejecución:

```bash
python main.py
```

## Seguridad

El análisis estático (Semgrep) y el escaneo de secretos (Gitleaks) corren en cada *push*
y PR (ver [workflow](.github/workflows/security.yml)). Las credenciales de la base de
datos no deben versionarse. Reporta vulnerabilidades según [SECURITY.md](SECURITY.md).

## Tecnologías

Python · Tkinter · MySQL · tabulate

---

Proyecto de Luis Enrique González Ramírez — [github.com/KikeGonRam](https://github.com/KikeGonRam)
