# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
# números impares desde 1 hasta ese número separados por comas.


def pedir_num():
    while True:
        try:
            num = str(input("Introduce un Nº: "))
            while int(num) < 0:
                if int(num) < 0:
                    print("**ERROR** Valor invalido introduce un Nº positivo.")
                    num = str(input("Introduce un Nº: "))
            return num
        except ValueError:
            if num.find(".") == True:
                print("**ERROR** Introduce un Nº sin decimales")
            elif num.isalpha() == True:
                print("**ERROR** Introduce un numero no una letra.")
    return


def convertir_num(num):
    espacio = ", "
    for i in range(1, int(num)+1, +1):
        if i%2 != 0:
            if i == 1:
                cadena = i
            else:
                cadena = str(cadena) + espacio + str(i)
    return cadena


def main():
    num = pedir_num()
    cadena = convertir_num(num)
    print(cadena)
    return 0

if __name__ == "__main__":
    main()






