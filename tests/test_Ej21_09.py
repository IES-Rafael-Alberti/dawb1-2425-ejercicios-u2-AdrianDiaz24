import pytest

from src.Condicionales.EJ21_09 import calcular_precio


def test_calcular_precio():
    assert calcular_precio(1) == "gratuita"
    assert calcular_precio(5) == 5
    assert calcular_precio(2) == "gratuita"
    assert calcular_precio(20) == 10
    assert calcular_precio(3) == "gratuita"
    assert calcular_precio(0) == "gratuita"
    assert calcular_precio(17) == 5
    assert calcular_precio(7) == 5
    assert calcular_precio(120) == 10