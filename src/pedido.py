from datetime import date
from src.producto import Producto

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

    def mostrarPedido(self):
        print("=== Verificación de Pedido === \n"
        f"ID del Pedido: {self.IdPedido}\n"
        f"Fecha: {self.fecha} \n"
        f"Estado: {self.estado} ")
        print(f"Productos Solicitados: ")  
        for p,cant in self.prodSoli:
            print(f" Nombre: {p.nombre} | Cantidad: {cant}")