# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario 
# ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


def pedir_num():
        num = str(input("Introduce un Nº entero: "))
        i = num.isdigit()
        while i == False or int(num) < 0:
            num = str(input("**ERROR** Introduce un Nº entero: "))
            i = num.isdigit()
        return num


def comprobar_num(num):
    if num%2 == 0:
        num_c = 1
    else:
        num_c = 0
    return num_c


def main():
    num_p = 0
    num_i = 0
    while True:
        num = pedir_num()
        if num == 0:
            print(f"\nTotal de Nº pares: {num_p}\nTotal de Nº impares: {num_i}\n")
            break
        else:
            long = len(num)
            for i in range(0, long, +1):
                num_c = comprobar_num(num[i])
    return 0

if __name__ == "__main__":
    main()