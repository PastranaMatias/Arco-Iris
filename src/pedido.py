from datetime import date

class Pedido:
    def __init__(self, IdPedido):
        self.IdPedido=IdPedido
        self.fecha=date.today()
        self.estado="Pendiente"
        self.prodSoli=[]

    def generarPedido(self, listaProduc):
        self.prodSoli=listaProduc
        self.estado="Solicitado"
        print("Pedido generado correctamente.")

    def actualizarEstado(self, nuevoEstado):
        self.estado = nuevoEstado
