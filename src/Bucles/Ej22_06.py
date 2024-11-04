#Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo, de altura el número introducido.


def pedir_num():
    num = int(input("Introduce un Nº entero: "))
    while num < 0:
        num = int(input("**ERROR** Valor invalido, itroduce uno valdio: "))
    return num


def construir_piramide(num):
    i = 0
    a = ""
    asterisco = "*"
    while i < num:
        a = a+asterisco
        i = i+1
    return a


def main():
    num = pedir_num()

    for i in range(0, num+1, +1):
        a = construir_piramide(i)
        print(a)
    return 0

if __name__ == "__main__":
    main()