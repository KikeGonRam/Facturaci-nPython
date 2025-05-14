class Cliente:
    def __init__(self, id, nombre, documento):
        self.id = id
        self.nombre = nombre
        self.documento = documento

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self, id, cliente_id, fecha):
        self.id = id
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.items = []

    def add_item(self, producto, cantidad):
        self.items.append({"producto": producto, "cantidad": cantidad})

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self.items)