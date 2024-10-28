# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.


def pedir_num():
    num =  int(input("Introduce un Nº entero positivo: "))
    while num < 0:
        num = int(input("**ERROR** Valor invalido, introduce uno valido: "))
    return num


def comprobar_impares(num):
    impares = ""
    espacio = " , "
    for i in range(1, num+1, +1):
        a = i%2
        if a != 0:
            if   i == 1:
                impares = str(impares) + str(i)
            else:
                impares = str(impares) + str(espacio) + str(i)
    return impares


def main():
    num = pedir_num()
    impares = comprobar_impares(num)

    print(impares)
    
    return 0

if __name__ == "__main__":
    main()