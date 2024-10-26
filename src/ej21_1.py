# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


def pedir_edad():
    edad = int(input("Introduce su edad: "))

    while edad < 0 or edad > 140:
        edad = int(input("**ERROR** Edad invalida itroduzca una edad entre 0 y 140: "))
    return edad


def main():
    edad = pedir_edad()
    print(edad)

    return 0

if __name__ == "__main__":
    main()