from interfaces.imostrable import IMostrable
from producto import Producto

class GestorProductos(IMostrable):
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, p: Producto):
        self.lista_productos.append(p)
        print("✅ Producto agregado correctamente.")

    def buscar_producto(self, nombre, marca, color=None):
        for p in self.lista_productos:
            if (p.nombre.lower() == nombre.lower() and 
                p.marca.lower() == marca.lower() and 
                ((p.color is None and color is None) or (p.color and color and p.color.lower() == color.lower()))):
                return p
        return None

    def modificar_stock(self, nombre, marca, color, cantidad):
        producto = self.buscar_producto(nombre, marca, color)
        if producto:
            try:
                producto.actualizar_stock(cantidad)
                print(f"Stock actualizado: {producto.nombre} ({producto.marca}, Color: {producto.color}) ahora tiene {producto.stock} unidades.")
            except ValueError as e:
                print(e)
        else:
            print("❌ Producto no encontrado.")

    def eliminar_producto(self, nombre, marca, color=None):
        producto = self.buscar_producto(nombre, marca, color)
        if producto:
            self.lista_productos.remove(producto)
            print(f"🗑️ Producto eliminado: {producto.nombre} ({producto.marca}, Color: {producto.color})")
        else:
            print("❌ Producto no encontrado para eliminar.")

    def mostrar(self):
        if not self.lista_productos:
            print("No hay productos registrados.")
        else:
            print("\n=== Lista de productos con precios de venta y stock ===")
            for p in self.lista_productos:
                p.mostrar()
