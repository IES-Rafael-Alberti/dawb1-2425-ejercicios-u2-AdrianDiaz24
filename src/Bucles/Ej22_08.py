# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1


def pedir_num():
    num = int(input("Introduce un Nº entero: "))
    return num


def construir_piramides(i):
    a = ""
    espacio = " "

    if i > 0:
        for i in range(1, i+1, +1):
            if i%2 != 0:
                if i == 1:
                    a = a+str(i)
                else:
                    a = a+espacio+str(i)
        a = a[::-1]
    else:
        for i in range(-1, i-1, -1):
            if i%2 != 0:
                if i == 1:
                    a = a+str(i)
                else:
                    a = a+espacio+str(i)
        a = a.replace("-", "")
        a = a[::-1]
    return a


def main():
    num = pedir_num()
    if num > 0:
        for i in range(1, num+1, +1):
            if i%2 != 0:
                a = construir_piramides(i)
                print(a)
    else:
        for i in range(-1, num-1, -1):
            if i%2 != 0:
                a = construir_piramides(i)
                print(a)
    return 0

if __name__ == "__main__":
    main()