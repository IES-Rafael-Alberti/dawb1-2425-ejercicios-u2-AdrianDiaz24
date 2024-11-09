import pytest

from src.Bucles.Ej22_10 import comprobar_primo


def test_comprobar_primo():
    assert comprobar_primo(11) == "es primo"
    assert comprobar_primo(4) == "no es primo"
    assert comprobar_primo(7) == "es primo"
    assert comprobar_primo(5) == "es primo"
    assert comprobar_primo(8) == "no es primo"
    assert comprobar_primo(6) == "no es primo"
    assert comprobar_primo(12) == "no es primo"
    assert comprobar_primo(29) == "es primo"
    assert comprobar_primo(23) == "es primo"
    assert comprobar_primo(24) == "no es primo"