from database import create_tables, add_cliente, add_producto, add_factura, add_factura_item
from database import get_all_clientes, get_all_productos, get_all_facturas, get_factura_detalles
from models import Cliente, Producto, Factura
from utils import format_table, save_factura_to_file
from dateutil.parser import parse
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    create_tables()
    while True:
        clear_screen()
        print("=== Sistema de Facturación ===")
        print("1. Agregar Cliente")
        print("2. Agregar Producto")
        print("3. Crear Factura")
        print("4. Listar Clientes")
        print("5. Listar Productos")
        print("6. Listar Facturas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear_screen()
            nombre = input("Nombre del cliente: ")
            documento = input("Documento del cliente: ")
            if add_cliente(nombre, documento):
                print("Cliente agregado exitosamente.")
            else:
                print("Error al agregar cliente.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            clear_screen()
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                if add_producto(nombre, precio):
                    print("Producto agregado exitosamente.")
                else:
                    print("Error al agregar producto.")
            except ValueError:
                print("El precio debe ser un número.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            clear_screen()
            clientes = get_all_clientes()
            if not clientes:
                print("No hay clientes registrados.")
                input("Presione Enter para continuar...")
                continue
            print(format_table(["ID", "Nombre", "Documento"], clientes))
            try:
                cliente_id = int(input("Seleccione el ID del cliente: "))
                fecha = parse(input("Fecha de la factura (YYYY-MM-DD): ")).strftime("%Y-%m-%d")
                factura_id = add_factura(cliente_id, fecha)
                if factura_id:
                    print("Factura creada. Ahora agregue los productos.")
                    while True:
                        productos = get_all_productos()
                        if not productos:
                            print("No hay productos registrados.")
                            break
                        print(format_table(["ID", "Nombre", "Precio"], productos))
                        producto_id = int(input("Seleccione el ID del producto (0 para terminar): "))
                        if producto_id == 0:
                            break
                        cantidad = int(input("Cantidad: "))
                        add_factura_item(factura_id, producto_id, cantidad)
                    detalles = get_factura_detalles(factura_id)
                    cliente = next((c for c in clientes if c[0] == cliente_id), None)
                    filename = save_factura_to_file(Factura(factura_id, cliente_id, fecha), cliente, detalles)
                    print(f"Factura guardada en {filename}")
                else:
                    print("Error al crear factura.")
            except ValueError:
                print("Entrada inválida.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            clear_screen()
            clientes = get_all_clientes()
            if clientes:
                print(format_table(["ID", "Nombre", "Documento"], clientes))
            else:
                print("No hay clientes registrados.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            clear_screen()
            productos = get_all_productos()
            if productos:
                print(format_table(["ID", "Nombre", "Precio"], productos))
            else:
                print("No hay productos registrados.")
            input("Presione Enter para continuar...")

        elif opcion == "6":
            clear_screen()
            facturas = get_all_facturas()
            if facturas:
                print(format_table(["ID", "Cliente", "Fecha"], facturas))
            else:
                print("No hay facturas registradas.")
            input("Presione Enter para continuar...")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()