import pytest

from src.Bucles.Ej22_05 import calcular_capital_o


def test_calcular_capital_o():
    assert calcular_capital_o(1000, 10, 1) == 100
    assert calcular_capital_o(5000, 10, 1) == 500
    assert calcular_capital_o(5500, 100, 1) == 5500
    assert calcular_capital_o(1000, 10, 3) == 121
    assert calcular_capital_o(2000, 10, 3) == 242

    