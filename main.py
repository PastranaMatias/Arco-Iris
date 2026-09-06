class Producto:
    def __init__(self, nombre, marca, precio, stock_inicial=0):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock_inicial

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def mostrar_confirmacion(self):
        print(f"✅ Producto registrado: {self.nombre} ({self.marca}) - Precio: ${self.precio}, Stock: {self.stock}")


def validar_precio(valor):
    try:
        precio = float(valor)
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return precio
    except ValueError:
        print("❌ Precio inválido. Ingrese un número válido.")
        return None


def validar_stock(valor):
    try:
        stock = int(valor)
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return stock
    except ValueError:
        print("❌ Stock inválido. Ingrese un número entero.")
        return None


# --- Simulación de formulario en consola ---
nombre = input("Ingrese nombre del producto: ")
marca = input("Ingrese marca del producto: ")

precio = None
while precio is None:
    precio = validar_precio(input("Ingrese precio del producto: "))

stock = None
while stock is None:
    stock = validar_stock(input("Ingrese cantidad inicial en stock: "))

# Guardar producto
nuevo = Producto(nombre, marca, precio, stock)

# Actualizar stock (ejemplo: ingreso de 5 unidades más)
nuevo.actualizar_stock(5)

# Mostrar confirmación
nuevo.mostrar_confirmacion()

# Realizar pruebas simples
if nuevo.stock >= 0 and nuevo.precio > 0:
    print("✅ Prueba OK: Producto válido.")
else:
    print("❌ Prueba fallida: Datos incorrectos.")
