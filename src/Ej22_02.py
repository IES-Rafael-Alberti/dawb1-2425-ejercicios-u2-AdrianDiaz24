# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def pedir_edad():
    edad = int(input("Introduce tu edad: "))
    while edad < 0 or edad > 130:
        edad = int(input("**ERROR** Valor invalido. Vuelva a introducir su edad: "))
    return edad


def main():
    edad = pedir_edad()
    return 0

if __name__ == "__main__":
    main()