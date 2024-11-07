# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta 
# atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir 
# uno correcto.


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



def convertir_num(num):
    espacio = ", "
    for i in range(int(num),-1 , -1):
            if i == int(num):
                cadena = str(i)
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

