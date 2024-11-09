import pytest

from src.Bucles.Ej22_18 import sumar_digitos


def test_sumar_digitos():
    assert sumar_digitos(55) == 10
    assert sumar_digitos(66) == 12
    assert sumar_digitos(1475) == 17
    assert sumar_digitos(748) == 19
    assert sumar_digitos(999) == 27
    assert sumar_digitos(7859) == 29
    assert sumar_digitos(999999999) == 81
    assert sumar_digitos(42) == 6
    assert sumar_digitos(1) == 1
    assert sumar_digitos(10) == 1

    