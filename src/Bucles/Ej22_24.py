# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


def pedir_num():
    num = str(input("Introduce un Nº entero positivo: "))
    while num.isdigit() == False:
        num = str(input("**ERROR** Valor invalido\n Introduce un Nº entero positivo:"))
    return num


def comprobar_paridad(num):
    contador = 0
    for i in range(1, int(num)+1, +1):
        if int(num)%i == 0:
            contador += 1
        else:
            continue
    if contador == 2:
        return 1
    else:
        return 0

    
    return 0


def main():
    contador = 0
    while True:
        num = pedir_num()
        if int(num) == 0:
            print(f"La cantidad de Nº primos introducidos es de {contador}")
            break
        elif int(num) == 1:
            contador += 1
        else:
            i = comprobar_paridad(num)
            contador += i

if __name__ == "__main__":
    main()















































