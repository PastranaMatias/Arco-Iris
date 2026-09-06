class Producto:
    def __init__(self, nombre, marca, precio, stock_inicial=0):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock_inicial

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def mostrar_confirmacion(self):
        print(f"✅ Producto: {self.nombre} ({self.marca}) - Precio: ${self.precio}, Stock: {self.stock}")
