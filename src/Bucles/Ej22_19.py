# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se 
# imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import time

def mostrar_menu():
    num = int(input("MENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    while num < 1 or num > 3:
        num = int(input("**ERROR** Valor invalido.\nMENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    return num


def programa_1():
    print("Elegiste la opcion 1\n")
    time.sleep(1)
    print("Ejecutando el programa.")
    time.sleep(1)
    print("Ejecutando el programa..")
    time.sleep(1)
    print("Ejecutando el programa...\n")
    time.sleep(1)
    print("**ERROR AL EJECUTAR EL PROGRAMA**\n")
    time.sleep(1)
    print("Volviendo al menu.\n")
    time.sleep(1)
    return 0


def listado():
    print("Elegiste la opcion 2\n")
    time.sleep(1)
    print("Imprimiendo el listado.")
    time.sleep(1)
    print("Imprimiendo el listado..")
    time.sleep(1)
    print("Imprimiendo el listado...\n")
    time.sleep(1)
    print("**ERROR AL IMPRIMIR EL LISTADO**\n")
    time.sleep(1)
    print("Volviendo al menu.\n")
    time.sleep(1)
    return 0


def salir():
    print("\nSaliendo.")
    time.sleep(1)
    print("Saliendo..")
    time.sleep(1)
    print("Saliendo...\n")
    time.sleep(1)
    print("Saliste")
    return 0



def main():
    num = mostrar_menu()
    while True:
        if num == 1:
            programa_1()
            num = mostrar_menu()
        elif num == 2:
            listado()
            num = mostrar_menu()
        elif  num == 3:
            salir()
            break
if __name__ == "__main__":
    main()