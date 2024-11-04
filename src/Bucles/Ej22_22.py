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


def main():
    num = pedir_num()
    return 0

if __name__ == "__main__":
    main()