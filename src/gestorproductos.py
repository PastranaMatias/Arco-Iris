from producto import Producto
from descuento import Descuento
from stock import Stock

class GestorProductos:
    def __init__(self):
        self.ListaProductos=[]

    def agregarProducto(self,p:Producto):
        self.ListaProductos.append(p)
        print("se agrego el producto")

  
    def aplicarDescuento(self, p: Producto, descuento: Descuento):
        return descuento.aplicar(p.precio)

    def verificarStock(self,p:Producto)->bool:
        stock=Stock(p.stock)
        return stock.verifica()

    def mostrarPreciosFinales(self):
        for produc in self.ListaProductos:
            print (f"{Producto(produc).nombre}:${Producto(produc).calcular_precio()}")
        