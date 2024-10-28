# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.


def pedir_num():
    num =  int(input("Introduce un Nº entero positivo: "))
    while num < 0:
        num = int(input("**ERROR** Valor invalido, introduce uno valido: "))
    return num


def main():
    num = pedir_num()
    return 0

if __name__ == "__main__":
    main()