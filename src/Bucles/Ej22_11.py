# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.


def introducir_palabra():
    palabra = str(input("Introduce una palabra: "))
    return palabra


def conseguir_letra(i, palabra):
    letra = palabra[i]
    return letra


def main():
    palabra = introducir_palabra()
    a = len(palabra)
    for i in range(0, a, +1):
        letra = conseguir_letra(i, palabra)
        print(letra)
    return 0

if __name__ == "__main__":
    main()