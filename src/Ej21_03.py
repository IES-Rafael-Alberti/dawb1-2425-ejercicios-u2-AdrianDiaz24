# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def pedir_num():
    num = float(input("Introduzca un Nº que dividir: "))
    return num


def pedir_divisor():
    divisor = float(input("Introduzca el divisor: "))
    while divisor == 0:
        print("**ERROR** Cualquier Nº dividido entre 0 es infinito")
        divisor = float(input("Introduzca otro divisor: "))
    return divisor


def main():
    num = pedir_num()
    divisor = pedir_divisor()
    print(f"-> {num}/{divisor} = ", num/divisor)
    return 0

if __name__ =="__main__":
    main()