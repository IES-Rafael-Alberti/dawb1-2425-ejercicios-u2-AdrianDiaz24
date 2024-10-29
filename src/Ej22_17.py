# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


def pedir_num():
    num = int(input("Introduce un Nº entero positivo: "))
    while num < 0:
        num = int(input("**ERROR** Introduce un Nº entero positivo: "))
    return num


def sumar_digitos(num) -> str:
    a = len(str(num))
    num = str(num)
    suma = 0
    for i in range(0, a, +1):
        b = num[i]
        suma = suma + int(b)
    return suma


def main():
    num = pedir_num()
    suma = sumar_digitos(num)
    print(f"La suma de los digitos del Nº dado es {suma}")
    return 0

if __name__ == "__main__":
    main()