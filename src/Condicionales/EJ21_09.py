# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


def pedir_edad():
    edad = int(input("Introduzca su edad: "))
    while edad < 0 or edad > 130:
        edad = int(input("**ERROR** Edad invalida, Introduzca una valida: "))
    return edad


def calcular_precio(edad):
    if edad < 4:
        precio = "gratuita"
    elif edad >= 4 and edad <= 18:
        precio = 5
    elif edad > 18:
        precio = 10
    return precio 


def main():
    edad = pedir_edad()
    precio = calcular_precio(edad)

    if edad < 4:
        print(f"Usted tiene {edad} años por lo cual su entrada es {precio}")
    else:
        print(f"Usted tiene {edad} años por lo cual su entrada cuesta {precio}€")

    return 0

if __name__ == "__main__":
    main()