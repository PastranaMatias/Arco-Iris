import pytest
from src.producto import Producto

def test_crear_producto_valido():
    p = Producto(1, "Pintura", "Sherwin", 1000, 10, "Rojo")
    assert p.nombre == "Pintura"
    assert p.marca == "Sherwin"
    assert p.precio == 1000
    assert p.stock == 10
    assert p.color == "Rojo"

def test_precio_invalido():
    with pytest.raises(ValueError):
        Producto(1, "Pintura", "Sherwin", -100, 10)

def test_stock_invalido():
    with pytest.raises(ValueError):
        Producto(1, "Pintura", "Sherwin", 100, -5)

def test_actualizar_stock_valido():
    p = Producto(1, "Pintura", "Sherwin", 100, 10)
    p.actualizar_stock(-3)
    assert p.stock == 7

def test_actualizar_stock_excede():
    p = Producto(1, "Pintura", "Sherwin", 100, 2)
    with pytest.raises(ValueError):
        p.actualizar_stock(-5)

def test_calcular_precio():
    p = Producto(1, "Pintura", "Sherwin", 100, 10)
    assert p.calcular_precio() == 130
