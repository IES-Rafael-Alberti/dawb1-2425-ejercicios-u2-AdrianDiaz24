# Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el 
# usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se 
# considera que termina una línea. Por cada línea completa, informar cuántos dígitos
#  numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que 
# componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

import time


def comprobar_cadena(cadena:str):
    contador = 0
    i = 0
    if cadena == "*":
        salir()
    else:
        long = len(cadena)
        while contador < 10 and i != long-1:
            for i in range(0, long, +1):
                comprobacion = cadena[i].isdigit()
                if comprobacion == False:
                    continue
                elif comprobacion == True:
                    contador += 1
                elif i == long:
                    return contador 
    return contador


def salir():
    print("Saliendo.")
    time.sleep(1)
    print("Saliendo..")
    time.sleep(1)
    print("Saliendo...")
    time.sleep(1)
    exit
    return 0


def main():
    contador = 0
    while True:
        cadena = str(input("Introduce el titulo de un libro: "))
        if cadena == "/":
            print(f"Linea completa: Aparecen {contador} digitos numericos")
            contador = 0
        else:
            i = comprobar_cadena(cadena)
            contador += i
        
    return 0

if __name__ == "__main__":
    main()