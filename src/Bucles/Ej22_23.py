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



def main():
    contador = 0
    contador_f = 0
    while True:
        cadena = str(input("Introduce el titulo de un libro: "))
        if cadena == "/":
            contador_f += 1
            if contador < 10:
                print(f"\nLinea completa: Aparecen {contador} digitos numericos\n")
                contador = 0
            else:
                print("\nLinea completa: Aparecen 9 digitos numericos\n")
                contador = 0
        elif cadena == "*":
                print(f"\nFin: Se leyeron {contador_f} lineas completas.\n")
                time.sleep(1)
                print("\nSaliendo.")
                time.sleep(1)
                print("Saliendo..")
                time.sleep(1)
                print("Saliendo...\n")
                time.sleep(1)
                break
        else:
            i = comprobar_cadena(cadena)
            contador += i
        
    return 0

if __name__ == "__main__":
    main()