from src.producto import Producto
from src.descuento import Descuento
from src.stock import Stock
from src.ticket import Ticket

class GestorProductos:
    def __init__(self):
        self.ListaProductos = []

    def agregarProducto(self, p: Producto):
        self.ListaProductos.append(p)
        print("Se agregó el producto")

    def aplicarDescuento(self, p: Producto, descuento: Descuento):
        return descuento.aplicar(p.precio)

    def verificarStock(self, p: Producto) -> bool:
        stock = Stock(p.stock)
        return stock.verifica()

    def mostrarPreciosFinales(self):
        for produc in self.ListaProductos:
            print(f"{produc.nombre}: ${produc.calcular_precio()}")

    def mostrarListaPrecios(self, descuento_efectivo: float, recargo_credito: float):
        """Tarjeta 4: lista de precios según medio de pago"""
        for producto in self.ListaProductos:
            precio_base = producto.calcular_precio()
            precio_efectivo = Descuento("efectivo", descuento_efectivo).aplicar(precio_base)
            precio_credito = Descuento("credito", recargo_credito).aplicar(precio_base)

            print(
                f"{producto.nombre} | Base: ${precio_base} | "
                f"Efectivo (-{descuento_efectivo}%): ${precio_efectivo} | "
                f"Crédito (+{recargo_credito}%): ${precio_credito}"
            )

    def generarTicket(self, items):
        ticket = Ticket()
        for idPro, cantidad in items:  # recorro de 2 en 2
            nuevop = self.buscarProducto(idPro)  # busco el producto y guardo
            if nuevop is None:
                print("No se encontró")
            else:
                ticket.agregarP(nuevop, cantidad)
        return ticket

    def buscarProducto(self, id_p):
        for productos in self.ListaProductos:  # recorro los productos
            if productos.id == id_p:  # comparo si son igual los id
                return productos  # si se encuentra lo retorna
        return None   # sino retorna None
