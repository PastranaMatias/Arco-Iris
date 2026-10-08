from src.producto import Producto
from src.gestorproductos import GestorProductos


def test_tarjeta5_integrador():

    producto = Producto(1,"Pintura","Sherwin",100,1,"Rojo")
    gestor = GestorProductos()
    gestor.agregarProducto(producto)

    producto.actualizar_stock(-1)

    assert gestor.verificarStock(producto) is False

    gestor.agregarPedido(producto)

    assert len(gestor.ListaPedidos) == 1
    assert gestor.ListaPedidos[0] == producto

    gestor.realizarPedido([(producto, 10)])

    assert producto.stock == 10

    assert len(gestor.ListaPedidos) == 0