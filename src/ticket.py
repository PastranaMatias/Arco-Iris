from datetime import date

class Ticket:    
    def __init__(self):
        # lista de tuplas (producto, cantidad)
        self.items = []

    def agregarP(self, producto, cantidad):
        # agrega el producto y la cantidad al ticket
        self.items.append((producto, cantidad))

    def calTotal(self):
        total = 0
        for producto, cantidad in self.items:
            # si el producto tiene calcular_precio(), lo usamos
            if hasattr(producto, "calcular_precio"):
                total += producto.calcular_precio() * cantidad
            else:
                total += producto.precio * cantidad
        return total

    def impriTiket(self):
        print("\n=== Ticket de Venta ===")
        for producto, cantidad in self.items:
            if hasattr(producto, "calcular_precio"):
                precio_unitario = producto.calcular_precio()
            else:
                precio_unitario = producto.precio
            print(f"ID: {producto.id} | {producto.nombre} x{cantidad} - ${precio_unitario * cantidad}")
        print(f"TOTAL: ${self.calTotal()}")

