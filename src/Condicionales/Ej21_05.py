# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


def pedir_edad():
    edad = int(input("Introduce tu edad: "))
    while edad < 0 or edad > 130:
        edad = int(input("**ERROR** Edad invalidad introduzca su edad nuevamente: "))
    return edad


def pedir_ganancias():
    ganancias = float(input("Introduce tus ingresos mensuales: "))
    while ganancias < 0:
        ganancias = int(input("**ERROR** Ingresos invalidados introduzca sus ingresos mensuales nuevamente: "))
    return ganancias




def main():
    edad = pedir_edad()
    ganancias = pedir_ganancias()
    
    if edad > 16 and ganancias >= 1000:
        print("Usted tiene que tributar.")
    else:
        print("Usted no tiene que tributar.")

    return 0

if __name__ == "__main__":
    main()