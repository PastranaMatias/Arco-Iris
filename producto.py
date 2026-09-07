class Producto:
    def __init__(self, nombre, marca, precio, stock_inicial=0):
        # Validaciones
        if not nombre or not marca:
            raise ValueError("❌ El nombre y la marca no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("❌ El precio debe ser mayor a 0.")
        if stock_inicial < 0:
            raise ValueError("❌ El stock inicial no puede ser negativo.")

        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.color = color
        self.stock = stock_inicial

    def actualizar_stock(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.stock:
            raise ValueError("❌ No se puede reducir más stock del disponible.")
        self.stock += cantidad

    def mostrar_confirmacion(self):
        print(f"✅ Producto: {self.nombre} ({self.marca}) - Precio: ${self.precio}, Stock: {self.stock}")

    



