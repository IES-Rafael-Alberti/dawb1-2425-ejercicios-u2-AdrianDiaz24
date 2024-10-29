# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se 
# imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


def mostrar_menu():
    num = int(input("MENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    while num < 1 or num > 3:
        num = int(input("**ERROR** Valor invalido.\nMENU\n1. comenzar programa\n2. imprimir listado\n3. finalizar programa\n -> "))
    return num


def main():
    num = mostrar_menu()
    return 0

if __name__ == "__main__":
    main()