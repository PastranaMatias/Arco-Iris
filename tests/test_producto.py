import pytest
from src.producto import Producto
from src.gestorproductos import GestorProductos

def test_crear_producto():
    p = Producto("Pintura", "Sherwin", 1000, 10)
    assert p.nombre == "Pintura"
    assert p.marca == "Sherwin"
    assert p.precio == 1000
    assert p.stock == 10

def test_registrar_producto_en_gestor():
    gestor = GestorProductos()
    p = Producto("Pintura", "Sherwin", 1000, 10)
    gestor.agregar_producto(p)
    assert p in gestor.lista_productos
    assert len(gestor.lista_productos) == 1
