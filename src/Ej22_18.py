# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario 
# fueron números pares.


def pedir_num():
    num = int(input("Introduce un Nº: "))
    while num < -1:
        num = int(input("**ERROR** Introduce un Nº: "))
    return num


def sumar_digitos(num) -> str:
    a = len(str(num))
    num = str(num)
    suma = 0
    for i in range(0, a, +1):
        b = num[i]
        suma = suma + int(b)
    return suma


def comprobar_paridad(num):
    paridad = 0
    if num%2 == 0:
        paridad = paridad+1
    return paridad


def main():
    print("Introduce el -1 para cerrar el programa.")
    num = pedir_num()
    while num != -1:
        paridad = comprobar_paridad(num)
        suma = sumar_digitos(num)
        print(f"La suma de los digitos del Nº dado es {suma}")
        num = pedir_num()
    print(f"La cantidad de Nº pares introducidos por usted es de {paridad}.")
    return 0

if __name__ == "__main__":
    main()