from dateutil.parser import parse
import tkinter as tk
from tkinter import ttk, messagebox
from database import create_tables, add_cliente, add_producto, add_factura, add_factura_item
from database import get_all_clientes, get_all_productos, get_all_facturas, get_factura_detalles
from utils import save_factura_to_file
from models import Factura

class FacturacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Facturación")
        self.root.geometry("800x600")

        # Crear pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        # Pestañas
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_productos = ttk.Frame(self.notebook)
        self.tab_facturas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_productos, text="Productos")
        self.notebook.add(self.tab_facturas, text="Facturas")

        # Inicializar pestañas
        self.setup_clientes_tab()
        self.setup_productos_tab()
        self.setup_facturas_tab()

        # Crear tablas
        create_tables()

    def setup_clientes_tab(self):
        """Configura la pestaña de clientes."""
        # Formulario
        tk.Label(self.tab_clientes, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.cliente_nombre = tk.Entry(self.tab_clientes)
        self.cliente_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="Documento:").grid(row=1, column=0, padx=5, pady=5)
        self.cliente_documento = tk.Entry(self.tab_clientes)
        self.cliente_documento.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.tab_clientes, text="Agregar Cliente", command=self.add_cliente).grid(row=2, column=0, columnspan=2, pady=10)

        # Tabla
        self.clientes_tree = ttk.Treeview(self.tab_clientes, columns=("ID", "Nombre", "Documento"), show="headings")
        self.clientes_tree.heading("ID", text="ID")
        self.clientes_tree.heading("Nombre", text="Nombre")
        self.clientes_tree.heading("Documento", text="Documento")
        self.clientes_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.clientes_tree.bind("<ButtonRelease-1>", self.select_cliente)

        tk.Button(self.tab_clientes, text="Actualizar Lista", command=self.update_clientes_table).grid(row=4, column=0, columnspan=2, pady=5)
        self.update_clientes_table()

    def add_cliente(self):
        """Agrega un cliente desde la interfaz."""
        nombre = self.cliente_nombre.get()
        documento = self.cliente_documento.get()
        if nombre and documento:
            if add_cliente(nombre, documento):
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente.")
                self.update_clientes_table()
                self.cliente_nombre.delete(0, tk.END)
                self.cliente_documento.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al agregar cliente. Verifique que el documento sea único.")
        else:
            messagebox.showwarning("Advertencia", "Complete todos los campos.")

    def update_clientes_table(self):
        """Actualiza la tabla de clientes."""
        for item in self.clientes_tree.get_children():
            self.clientes_tree.delete(item)
        clientes = get_all_clientes()
        for cliente in clientes:
            self.clientes_tree.insert("", tk.END, values=cliente)

    def select_cliente(self, event):
        """Selecciona un cliente de la tabla."""
        selected = self.clientes_tree.selection()
        if selected:
            values = self.clientes_tree.item(selected[0])["values"]
            self.cliente_nombre.delete(0, tk.END)
            self.cliente_documento.delete(0, tk.END)
            self.cliente_nombre.insert(0, values[1])
            self.cliente_documento.insert(0, values[2])

    def setup_productos_tab(self):
        """Configura la pestaña de productos."""
        tk.Label(self.tab_productos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.producto_nombre = tk.Entry(self.tab_productos)
        self.producto_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab_productos, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
        self.producto_precio = tk.Entry(self.tab_productos)
        self.producto_precio.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.tab_productos, text="Agregar Producto", command=self.add_producto).grid(row=2, column=0, columnspan=2, pady=10)

        self.productos_tree = ttk.Treeview(self.tab_productos, columns=("ID", "Nombre", "Precio"), show="headings")
        self.productos_tree.heading("ID", text="ID")
        self.productos_tree.heading("Nombre", text="Nombre")
        self.productos_tree.heading("Precio", text="Precio")
        self.productos_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.productos_tree.bind("<ButtonRelease-1>", self.select_producto)

        tk.Button(self.tab_productos, text="Actualizar Lista", command=self.update_productos_table).grid(row=4, column=0, columnspan=2, pady=5)
        self.update_productos_table()

    def add_producto(self):
        """Agrega un producto desde la interfaz."""
        nombre = self.producto_nombre.get()
        precio = self.producto_precio.get()
        try:
            precio = float(precio)
            if nombre:
                if add_producto(nombre, precio):
                    messagebox.showinfo("Éxito", "Producto agregado exitosamente.")
                    self.update_productos_table()
                    self.producto_nombre.delete(0, tk.END)
                    self.producto_precio.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Error al agregar producto.")
            else:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número.")

    def update_productos_table(self):
        """Actualiza la tabla de productos."""
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)
        productos = get_all_productos()
        for producto in productos:
            self.productos_tree.insert("", tk.END, values=producto)

    def select_producto(self, event):
        """Selecciona un producto de la tabla."""
        selected = self.productos_tree.selection()
        if selected:
            values = self.productos_tree.item(selected[0])["values"]
            self.producto_nombre.delete(0, tk.END)
            self.producto_precio.delete(0, tk.END)
            self.producto_nombre.insert(0, values[1])
            self.producto_precio.insert(0, values[2])

    def setup_facturas_tab(self):
        """Configura la pestaña de facturas."""
        tk.Label(self.tab_facturas, text="Cliente:").grid(row=0, column=0, padx=5, pady=5)
        self.cliente_combo = ttk.Combobox(self.tab_facturas)
        self.cliente_combo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab_facturas, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.factura_fecha = tk.Entry(self.tab_facturas)
        self.factura_fecha.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.tab_facturas, text="Crear Factura", command=self.create_factura).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.tab_facturas, text="Guardar Factura", command=self.save_factura).grid(row=2, column=2, pady=10)

        self.facturas_tree = ttk.Treeview(self.tab_facturas, columns=("ID", "Cliente", "Fecha"), show="headings")
        self.facturas_tree.heading("ID", text="ID")
        self.facturas_tree.heading("Cliente", text="Cliente")
        self.facturas_tree.heading("Fecha", text="Fecha")
        self.facturas_tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        tk.Button(self.tab_facturas, text="Actualizar Lista", command=self.update_facturas_table).grid(row=4, column=0, columnspan=3, pady=5)
        self.update_facturas_table()

        # Frame para ítems de factura
        self.items_frame = ttk.LabelFrame(self.tab_facturas, text="Ítems de Factura")
        self.items_frame.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self.items_frame, text="Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.producto_combo = ttk.Combobox(self.items_frame)
        self.producto_combo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.items_frame, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        self.item_cantidad = tk.Entry(self.items_frame)
        self.item_cantidad.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.items_frame, text="Agregar Ítem", command=self.add_item).grid(row=2, column=0, columnspan=2, pady=5)

        self.items_tree = ttk.Treeview(self.items_frame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings")
        self.items_tree.heading("Producto", text="Producto")
        self.items_tree.heading("Precio", text="Precio")
        self.items_tree.heading("Cantidad", text="Cantidad")
        self.items_tree.heading("Subtotal", text="Subtotal")
        self.items_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.current_factura_id = None
        self.update_comboboxes()

    def update_comboboxes(self):
        """Actualiza los combobox de clientes y productos."""
        clientes = get_all_clientes()
        self.cliente_combo["values"] = [f"{c[0]} - {c[1]}" for c in clientes]
        productos = get_all_productos()
        self.producto_combo["values"] = [f"{p[0]} - {p[1]}" for p in productos]

    def create_factura(self):
        """Crea una nueva factura."""
        cliente = self.cliente_combo.get()
        fecha = self.factura_fecha.get()
        try:
            if cliente and fecha:
                cliente_id = int(cliente.split(" - ")[0])
                fecha = parse(fecha).strftime("%Y-%m-%d")
                factura_id = add_factura(cliente_id, fecha)
                if factura_id:
                    self.current_factura_id = factura_id
                    messagebox.showinfo("Éxito", f"Factura #{factura_id} creada. Agregue ítems.")
                    self.update_facturas_table()
                    self.update_comboboxes()
                    for item in self.items_tree.get_children():
                        self.items_tree.delete(item)
                else:
                    messagebox.showerror("Error", "Error al crear factura.")
            else:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido.")

    def add_item(self):
        """Agrega un ítem a la factura actual."""
        if not self.current_factura_id:
            messagebox.showwarning("Advertencia", "Primero cree una factura.")
            return
        producto = self.producto_combo.get()
        cantidad = self.item_cantidad.get()
        try:
            if producto and cantidad:
                producto_id = int(producto.split(" - ")[0])
                cantidad = int(cantidad)
                if add_factura_item(self.current_factura_id, producto_id, cantidad):
                    detalles = get_factura_detalles(self.current_factura_id)
                    for item in self.items_tree.get_children():
                        self.items_tree.delete(item)
                    for detalle in detalles:
                        subtotal = detalle[1] * detalle[2]
                        self.items_tree.insert("", tk.END, values=(detalle[0], detalle[1], detalle[2], subtotal))
                    self.item_cantidad.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Error al agregar ítem.")
            else:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número.")

    def save_factura(self):
        """Guarda la factura actual en un archivo."""
        if not self.current_factura_id:
            messagebox.showwarning("Advertencia", "No hay factura seleccionada.")
            return
        detalles = get_factura_detalles(self.current_factura_id)
        facturas = get_all_facturas()
        factura = next((f for f in facturas if f[0] == self.current_factura_id), None)
        if factura:
            clientes = get_all_clientes()
            cliente = next((c for c in clientes if c[0] == factura[1]), None)
            if cliente:
                filename = save_factura_to_file(
                    Factura(self.current_factura_id, factura[1], factura[2]),
                    cliente,
                    detalles
                )
                messagebox.showinfo("Éxito", f"Factura guardada en {filename}")
            else:
                messagebox.showerror("Error", "Cliente no encontrado.")
        else:
            messagebox.showerror("Error", "Factura no encontrada.")

    def update_facturas_table(self):
        """Actualiza la tabla de facturas."""
        for item in self.facturas_tree.get_children():
            self.facturas_tree.delete(item)
        facturas = get_all_facturas()
        for factura in facturas:
            self.facturas_tree.insert("", tk.END, values=factura)