class Producto:
    def __init__(self, nombre, marca, precio, stock_inicial=0,color=None):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.color = color
        self.stock = stock_inicial

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def mostrar_confirmacion(self):
        print(f"Producto: {self.nombre} ({self.marca}) - Precio: ${self.precio}, Stock: {self.stock},Color:{self.color}")

    #Funcion para validar que le producto no tengo valores erroneos
    def validar_datos(self): 
        if not self.nombre or self.nombre.strip() == "":
            return False

        if not self.marca or self.marca.strip() == "":
            return False
        
        if not self.color or self.color.strip() == "":
                    return False
        if self.precio <= 0:
            return False

        if self.stock < 0:
            return False

        return True
    #Agrego la funcion para calcular el precio, precio por la cantidad
    def calcular_precio(self):
        return self.precio * self.cantidad