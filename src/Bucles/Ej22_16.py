# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


def pedir_num():
    num = int(input("Introduce un Nº entero positivo: "))
    while num < 0:
        num = int(input("**ERROR** Introduce un Nº entero positivo: "))
    return num


def comprobar_num(num, mayor):
    a = mayor
    if num > a:
        a = num
    return a



def main():
    num = pedir_num()
    mayor = 0
    while num != 0:
        mayor = comprobar_num(num, mayor)
        num = pedir_num()
    print(f"El mayor Nº escrito era el {mayor}.")
    return 0

if __name__ == "__main__":
    main()