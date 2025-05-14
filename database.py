import sqlite3
from sqlite3 import Error

def create_connection():
    """Crea una conexión a la base de datos SQLite."""
    conn = None
    try:
        conn = sqlite3.connect("facturacion.db")
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conn

def create_tables():
    """Crea las tablas necesarias en la base de datos."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Tabla de clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    documento TEXT NOT NULL UNIQUE
                )
            """)
            # Tabla de productos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL
                )
            """)
            # Tabla de facturas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS facturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    fecha TEXT NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                )
            """)
            # Tabla de ítems de factura
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS factura_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    factura_id INTEGER NOT NULL,
                    producto_id INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL,
                    FOREIGN KEY (factura_id) REFERENCES facturas (id),
                    FOREIGN KEY (producto_id) REFERENCES productos (id)
                )
            """)
            conn.commit()
        except Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            conn.close()

def add_cliente(nombre, documento):
    """Agrega un cliente a la base de datos."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre, documento) VALUES (?, ?)", (nombre, documento))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al agregar cliente: {e}")
        return None
    finally:
        conn.close()

def add_producto(nombre, precio):
    """Agrega un producto a la base de datos."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al agregar producto: {e}")
        return None
    finally:
        conn.close()

def add_factura(cliente_id, fecha):
    """Crea una nueva factura."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO facturas (cliente_id, fecha) VALUES (?, ?)", (cliente_id, fecha))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear factura: {e}")
        return None
    finally:
        conn.close()

def add_factura_item(factura_id, producto_id, cantidad):
    """Agrega un ítem a una factura."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO factura_items (factura_id, producto_id, cantidad) VALUES (?, ?, ?)", 
                       (factura_id, producto_id, cantidad))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al agregar ítem a factura: {e}")
        return None
    finally:
        conn.close()

def get_all_clientes():
    """Obtiene todos los clientes."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener clientes: {e}")
        return []
    finally:
        conn.close()

def get_all_productos():
    """Obtiene todos los productos."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener productos: {e}")
        return []
    finally:
        conn.close()

def get_all_facturas():
    """Obtiene todas las facturas con detalles."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT f.id, c.nombre, f.fecha 
            FROM facturas f 
            JOIN clientes c ON f.cliente_id = c.id
        """)
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener facturas: {e}")
        return []
    finally:
        conn.close()

def get_factura_detalles(factura_id):
    """Obtiene los detalles de una factura específica."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.nombre, p.precio, fi.cantidad 
            FROM factura_items fi 
            JOIN productos p ON fi.producto_id = p.id 
            WHERE fi.factura_id = ?
        """, (factura_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener detalles de factura: {e}")
        return []
    finally:
        conn.close()