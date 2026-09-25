from producto import Producto
from descuento import Descuento
from stock import Stock
from ticket import Ticket

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
        
    def generarTicket(self,items):
        ticket=Ticket()
    
        for idPro, cantida in items:  #recorro de 2 en 2
            nuevop=self.buscarProducto(idPro) #busco el producto y guardo
    
            if nuevop is None:
                print ("Nose encontro")  #sino se enconcuentra salta aca
                      #encontrando    

            #if nuevop and self.verificarStock(nuevop) and nuevop.stock>=cantida:#veo si hay stock o si hay mas de lo q pido
            else:
                #print(nuevop.stock>=cantida)
                ticket.agregarP(nuevop,cantida)    #agrego el produc, y la canti
                #nuevop.actualizar_stock(nuevop.stock-cantida)#actualizo el stock
                #print(nuevop.stock>=cantida)
        return (ticket)        
    
    
    def buscarProducto(self,id_p):
        for productos in self.ListaProductos: #recorro los productos
                
            if productos.id==id_p: #busco y comparo si son igual los id
                return productos # si se encuentra lo retorna
            
        return None   #sino retorna None