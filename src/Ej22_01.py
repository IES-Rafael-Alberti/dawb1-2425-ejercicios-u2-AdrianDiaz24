# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


def pedir_palabra():
    palabra = str(input("Introduce una palabra: "))
    while not palabra.isalpha() == True:
        palabra = str(input("**ERROR** Palabra invalida, Introduce una valida: "))
    return palabra


def main():
    palabra = pedir_palabra()

    for i in range(0,10, +1):
        print(palabra)

    return 0

if __name__ == "__main__":
    main()