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
    if int(num)%2 == 0:
        num_c = 1
    else:
        num_c = 0
    return num_c


def main():
    num_p_t = 0
    num_i_t = 0
    while True:
        num_p = 0
        num_i = 0

        num = pedir_num()

        if int(num) == 0:
            print(f"\nTotal de digitos pares contados: {num_p_t}\nTotal de digitos impares contados: {num_i_t}\n")
            break
        else:
            long = len(num)
            for i in range(0, long, +1):
                num_c = comprobar_num(num[i])
                if num_c == 1:
                    num_p += 1
                    num_p_t += 1
                else:
                    num_i += 1
                    num_i_t += 1
            print(f"\nTotal de digitos pares: {num_p}\nTotal de digitos impares: {num_i}\n")

    return 0

if __name__ == "__main__":
    main()