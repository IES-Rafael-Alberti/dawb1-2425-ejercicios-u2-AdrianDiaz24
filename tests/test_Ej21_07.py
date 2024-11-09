import pytest

from src.Condicionales.Ej21_07 import calcular_impositivo


def test_calcular_impositivo():
    assert calcular_impositivo(1500) == "5%"
    assert calcular_impositivo(17482) == "15%"
    assert calcular_impositivo(7895) == "5%"
    assert calcular_impositivo(26845) == "20%"
    assert calcular_impositivo(40578) == "30%"
    assert calcular_impositivo(59000) == "30%"
    assert calcular_impositivo(60001) == "45%"
    assert calcular_impositivo(75864) == "45%"
    assert calcular_impositivo(35000) == "30%"