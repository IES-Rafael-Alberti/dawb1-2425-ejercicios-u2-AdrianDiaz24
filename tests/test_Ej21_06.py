import pytest

from src.Condicionales.Ej21_06 import comprobar_grupo


def test_comprobar_grupo():
    assert comprobar_grupo("a", "H") == "A"
    assert comprobar_grupo("a", "M") == "A"
    assert comprobar_grupo("l", "M") == "A"
    assert comprobar_grupo("m", "H") == "A"
    assert comprobar_grupo("z", "H") == "B"
    assert comprobar_grupo("z", "M") == "B"
    assert comprobar_grupo("n", "H") == "B"
    assert comprobar_grupo("m", "M") == "B"