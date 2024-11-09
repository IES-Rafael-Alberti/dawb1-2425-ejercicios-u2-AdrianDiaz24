import pytest

from src.Condicionales.Ej21_08 import calcular_bonus


def test_calcular_bonus():
    assert calcular_bonus(0.0) == 0.0
    assert calcular_bonus(0.4) == 960.0
    assert calcular_bonus(0.6) == 1440.0
    assert calcular_bonus(1.0) == 2400.0
    assert calcular_bonus(0.8) == 1920.0
    assert calcular_bonus(5.0) == 12000.0
    assert calcular_bonus(1.3) == 3120.0