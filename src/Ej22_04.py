# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.


def pedir_num():
    num = int(input("Introduce un Nº entero positivo: "))
    while num < 0:
        num = int((input("**ERROR** Valor invalido, introduzaca uno valido: ")))
    return num


def contar_cuenta_atras(num):
    cuenta_atras = ""
    espacio = ", "
    for i in range(num, -1, -1):
        if i == num:
            cuenta_atras = cuenta_atras + str(i)
        else:
            cuenta_atras = cuenta_atras + espacio + str(i)
    return cuenta_atras


def main():
    num = pedir_num()
    cuenta_atras = contar_cuenta_atras(num)
    print(cuenta_atras)
    return 0

if __name__ == "__main__":
    main()