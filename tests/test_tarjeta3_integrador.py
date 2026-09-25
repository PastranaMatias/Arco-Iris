from src.producto import Producto
from src.gestorproductos import GestorProductos
from src.ticket import Ticket
from src.descuento import Descuento

def test_tarjeta3_integrador():
    # CUANDO quiero cobrar con ticket y descuento
    p1 = Producto(3, "Rodillo", "Pentrilo", 1000, 2)
    p2 = Producto(4, "Barniz", "Akzo", 2000, 1)

    gestor = GestorProductos()
    gestor.agregarProducto(p1)
    gestor.agregarProducto(p2)

    # Generar ticket con productos
    ticket = Ticket()
    ticket.agregarP(p1, 1)
    ticket.agregarP(p2, 1)

    # Total sin descuento
    total_sin_descuento = ticket.calTotal()
    assert total_sin_descuento == p1.calcular_precio() + p2.calcular_precio()

    # Aplicar descuento en efectivo (10%)
    descuento_efectivo = Descuento("efectivo", 10)
    total_con_descuento = descuento_efectivo.aplicar(total_sin_descuento)
    assert total_con_descuento == total_sin_descuento * 0.9

    # Aplicar recargo con crédito (15%)
    descuento_credito = Descuento("credito", 15)
    total_con_credito = descuento_credito.aplicar(total_sin_descuento)
    assert total_con_credito == total_sin_descuento * 1.15
