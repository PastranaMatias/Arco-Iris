from interfaces.imostrable import IMostrable

class Producto(IMostrable):
    def __init__(self, nombre, marca, precio_costo, stock_inicial=0, color=None):
        if not nombre or not marca:
            raise ValueError("❌ El nombre y la marca no pueden estar vacíos.")
        if precio_costo <= 0:
            raise ValueError("❌ El precio de costo debe ser mayor a 0.")
        if stock_inicial < 0:
            raise ValueError("❌ El stock inicial no puede ser negativo.")
        if color is not None and not color.strip():
            raise ValueError("❌ El color no puede estar vacío si se especifica.")

        self.nombre = nombre
        self.marca = marca
        self.precio_costo = precio_costo
        self.stock = stock_inicial
        self.color = color

    def calcular_precio_venta(self):
        return round(self.precio_costo * 1.30, 2)

    def actualizar_stock(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.stock:
            raise ValueError("❌ No se puede reducir más stock del disponible.")
        self.stock += cantidad

    def mostrar(self):
        info_color = f", Color: {self.color}" if self.color else ""
        print(f"{self.nombre} ({self.marca}{info_color}) - Precio venta: ${self.calcular_precio_venta()} - Stock: {self.stock}")
