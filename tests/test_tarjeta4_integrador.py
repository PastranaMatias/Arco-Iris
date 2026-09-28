from src.producto import Producto
from src.gestorproductos import GestorProductos
from src.descuento import Descuento

def test_tarjeta4_integrador():
    # CUANDO tengo productos cargados
    p1 = Producto(1, "Pintura", "Grre", 100, 5, "Rojo")
    p2 = Producto(2, "Barniz", "Akzo", 200, 7, "Azul")

    gestor = GestorProductos()
    gestor.agregarProducto(p1)
    gestor.agregarProducto(p2)

    # QUIERO tener lista de precios según medio de pago
    precio_base_p1 = p1.calcular_precio()
    precio_base_p2 = p2.calcular_precio()

    # Efectivo (10% descuento)
    precio_efectivo_p1 = Descuento("efectivo", 10).aplicar(precio_base_p1)
    precio_efectivo_p2 = Descuento("efectivo", 10).aplicar(precio_base_p2)

    # Crédito (15% recargo)
    precio_credito_p1 = Descuento("credito", 15).aplicar(precio_base_p1)
    precio_credito_p2 = Descuento("credito", 15).aplicar(precio_base_p2)

    # Validaciones
    assert precio_base_p1 == 130   # 100 + 30%
    assert precio_base_p2 == 260   # 200 + 30%
    assert precio_efectivo_p1 == 117   # 130 - 10%
    assert precio_efectivo_p2 == 234   # 260 - 10%
    assert precio_credito_p1 == 149.5  # 130 + 15%
    assert precio_credito_p2 == 299    # 260 + 15%
