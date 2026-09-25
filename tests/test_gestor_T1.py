import pytest
from src.producto import Producto
from src.gestorproductos import GestorProductos

def test_agregar_producto():
    gestor = GestorProductos()
    p = Producto(1, "Barniz", "Akzo", 500, 5)
    gestor.agregarProducto(p)
    assert p in gestor.ListaProductos

def test_buscar_producto_existente():
    gestor = GestorProductos()
    p = Producto(1, "Barniz", "Akzo", 500, 5)
    gestor.agregarProducto(p)
    encontrado = gestor.buscarProducto(1)
    assert encontrado == p

def test_buscar_producto_inexistente():
    gestor = GestorProductos()
    assert gestor.buscarProducto(99) is None
