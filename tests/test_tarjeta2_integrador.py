from src.producto import Producto
from src.gestorproductos import GestorProductos
from src.stock import Stock

def test_tarjeta2_integrador():
    # CUANDO quiero verificar stock y precios
    producto = Producto(2, "Barniz", "Akzo", 200, 5, "Transparente")

    # Registrar en el gestor
    gestor = GestorProductos()
    gestor.agregarProducto(producto)

    # QUIERO verificar stock usando la clase Stock
    stock = Stock(producto.stock)
    assert stock.verifica() is True
    assert producto.stock == 5

    # QUIERO ver el precio final con ganancia
    precio_final = producto.calcular_precio()
    assert precio_final == 260  # 200 + 30%

    # PARA poder mostrar precios finales en el gestor
    encontrado = gestor.buscarProducto(2)
    assert encontrado is not None
    assert encontrado.nombre == "Barniz"
    assert encontrado.calcular_precio() == 260
