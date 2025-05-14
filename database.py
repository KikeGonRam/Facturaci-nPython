import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea una conexión a la base de datos MySQL."""
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Reemplaza con tu usuario de MySQL
            password="",  # Reemplaza con tu contraseña de MySQL
            database="facturacion;",
            port=3306
        )
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conn

def create_tables():
    """Crea las tablas necesarias en la base de datos MySQL."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Tabla de clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    documento VARCHAR(50) NOT NULL UNIQUE
                )
            """)
            # Tabla de productos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    precio DECIMAL(10,2) NOT NULL
                )
            """)
            # Tabla de facturas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS facturas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente_id INT NOT NULL,
                    fecha DATE NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                )
            """)
            # Tabla de ítems de factura
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS factura_items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    factura_id INT NOT NULL,
                    producto_id INT NOT NULL,
                    cantidad INT NOT NULL,
                    FOREIGN KEY (factura_id) REFERENCES facturas(id),
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
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
        cursor.execute("INSERT INTO clientes (nombre, documento) VALUES (%s, %s)", (nombre, documento))
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
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
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
        cursor.execute("INSERT INTO facturas (cliente_id, fecha) VALUES (%s, %s)", (cliente_id, fecha))
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
        cursor.execute("INSERT INTO factura_items (factura_id, producto_id, cantidad) VALUES (%s, %s, %s)", 
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
            WHERE fi.factura_id = %s
        """, (factura_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener detalles de factura: {e}")
        return []
    finally:
        conn.close()