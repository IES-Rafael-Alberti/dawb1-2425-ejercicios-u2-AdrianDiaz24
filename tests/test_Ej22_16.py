import pytest

from src.Bucles.Ej22_16 import comprobar_num


def test_comprobar_num():
    assert comprobar_num(11, 12) == 12
    assert comprobar_num(58, 1) == 58
    assert comprobar_num(45, 44) == 45
    assert comprobar_num(0, 10) == 10
    assert comprobar_num(42, 41) == 42
    assert comprobar_num(14, 4) == 14
    assert comprobar_num(5681, 5687) == 5687
    assert comprobar_num(1,2) == 2
    assert comprobar_num(1,-1) == 1