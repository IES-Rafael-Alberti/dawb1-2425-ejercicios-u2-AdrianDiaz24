# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def pedir_num():
    num = int(input("Introduzca un Nº entero: "))
    return num


def comprobar_paridad(num):
    a = num%2
    if a == 0:
        print(f"{num} es par.")
    else:
        print(f"{num} es impar.")

    return 0


def main():
    num = pedir_num()
    comprobar_paridad(num)
    return 0

if __name__ == "__main__":
    main()