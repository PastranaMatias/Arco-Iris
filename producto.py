class Producto:
    def __init__(self, nombre, marca, precio, stock_inicial=0, color=None):
        # Validaciones
        if not nombre or not marca:
            raise ValueError("El nombre y la marca no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        if stock_inicial < 0:
            raise ValueError("El stock inicial no puede ser negativo.")
        if color is not None and not color.strip():
            raise ValueError("El color no puede estar vacío si se especifica.")

        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock_inicial
        self.color = color  # nuevo atributo

    def actualizar_stock(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.stock:
            raise ValueError("No se puede reducir más stock del disponible.")
        self.stock += cantidad

    def mostrar_confirmacion(self):
        info_color = f", Color: {self.color}" if self.color else ""
        print(f"Producto: {self.nombre} ({self.marca}) - Precio: ${self.precio}, Stock: {self.stock}{info_color}")

    



