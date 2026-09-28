from src.producto import Producto
from src.gestorproductos import GestorProductos

def test_tarjeta1_integrador():
    # CUANDO llega un producto al depósito
    producto = Producto(1, "Pintura", "Sherwin", 100, 10, "Rojo")

    # QUIERO ingresar nombre, marca y precio
    assert producto.nombre == "Pintura"
    assert producto.marca == "Sherwin"
    assert producto.precio == 100

    # PARA poder generar stock y precios
    assert producto.stock == 10
    assert producto.calcular_precio() == 130  # 100 + 30%

    # Registrar en el gestor
    gestor = GestorProductos()
    gestor.agregarProducto(producto)

    # Validar que el producto quedó en la lista
    encontrado = gestor.buscarProducto(1)
    assert encontrado is not None
    assert encontrado.nombre == "Pintura"
    assert encontrado.marca == "Sherwin"
    assert encontrado.precio == 100
    assert encontrado.stock == 10
