# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se 
# imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


def mostrar_menu():
    num = int(input("MENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    while num < 1 or num > 3:
        num = int(input("**ERROR** Valor invalido.\nMENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    return num


def programa_1():
    print("Elegiste la opcion 1\nEjecutando el programa.\nEjecutando el programa..\nEjecutando el programa...\n**ERROR AL EJECUTAR EL PROGRAMA**\nVolviendo al menu. ")
    return 0


def listado():
    print("Elegiste la opcion 2\nImprimiendo el listado.\nImprimiendo el listado..\nImprimiendo el listado...\n**ERROR AL IMPRIMIR EL LISTADO**\nVolviendo al menu. ")
    return 0



def main():
    num = mostrar_menu()
    while num != 3:
        if num == 1:
            programa_1()
            num = mostrar_menu()
        elif num == 2:
            listado()
            num = mostrar_menu()
        else:
            print("salinedo...")
    return 0
if __name__ == "__main__":
    main()