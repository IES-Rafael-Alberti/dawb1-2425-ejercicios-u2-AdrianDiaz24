import pytest

from src.Bucles.Ej22_23 import comprobar_cadena


def test_comprobar_cadena():
    assert comprobar_cadena("Los 2 cerditos.") == 1
    assert comprobar_cadena("Las 2000 lunas") == 4
    assert comprobar_cadena("manolo y las 3 manolas") == 1
    assert comprobar_cadena("manolete y el ultimo deseo") == 0
    assert comprobar_cadena("911 historia de un operador de emergencia") == 3
    assert comprobar_cadena("23 años del 11/S") == 4
    assert comprobar_cadena("-25 la aventura delos nemero negativos") == 2
    assert comprobar_cadena("Manuel y Manuela la historia de su vida") == 0
    assert comprobar_cadena("Los 3 sordos") == 1
    assert comprobar_cadena("Adalin y los 3 deseos a los 2 mamarachos") == 2
    assert comprobar_cadena("Hasta los cojones de inventarme titulos") == 0