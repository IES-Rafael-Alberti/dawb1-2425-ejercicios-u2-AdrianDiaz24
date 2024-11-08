import pytest

from src.Bucles.Ej22_25 import comprobar_palabras


def test_commprobar_palabras():
    assert comprobar_palabras("Los 2 cerditos") == "cerditos"
    assert comprobar_palabras("Las 2000 lunas") == "lunas"
    assert comprobar_palabras("manolo y las 3 manolas") == "manolas"
    assert comprobar_palabras("manolete y el ultimo deseo") == "manolete"
    assert comprobar_palabras("911 historia de un operador de emergencias") == "emergencias"
    assert comprobar_palabras("23 años del 11/S") == "años"
    assert comprobar_palabras("-25 la aventura delos nemero negativos") == "negativos"
    assert comprobar_palabras("Manuel y Manuela la historia de su vida") == "historia"
    assert comprobar_palabras("Los 3 sordos") == "sordos"
    assert comprobar_palabras("Adalin y los 3 deseos a los 2 mamarachos") == "mamarachos"