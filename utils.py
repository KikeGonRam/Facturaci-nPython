from tabulate import tabulate
from datetime import datetime
import os

def format_table(headers, data):
    """Formatea datos en una tabla usando tabulate."""
    return tabulate(data, headers=headers, tablefmt="grid")

def save_factura_to_file(factura, cliente, detalles):
    """Guarda la factura en un archivo de texto."""
    filename = f"factura_{factura.id}.txt"
    total = sum(detalle[1] * detalle[2] for detalle in detalles)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Factura #{factura.id}\n")
        f.write(f"Cliente: {cliente[1]}\n")
        f.write(f"Fecha: {factura.fecha}\n")
        f.write("-" * 40 + "\n")
        f.write("Producto | Precio | Cantidad | Subtotal\n")
        f.write("-" * 40 + "\n")
        for detalle in detalles:
            subtotal = detalle[1] * detalle[2]
            f.write(f"{detalle[0]} | {detalle[1]} | {detalle[2]} | {subtotal}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total: {total}\n")
    return filename