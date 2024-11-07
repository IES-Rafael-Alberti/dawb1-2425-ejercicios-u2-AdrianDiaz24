# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha 
# cumplido (desde 1 hasta su edad).


def pedir_edad():
    while True:
        try:
            edad = str(input("Introduce tu edad: "))
            while int(edad) < 0 or int(edad) > 140:
                if int(edad) < 0:
                    print("**ERROR** Tu edad no puede ser negativa.")
                    edad = str(input("Introduce tu edad: "))
                elif int(edad) > 140:
                    print("**ERROR** No te flipes que no puedes terer mas de 140 años.")
                    edad = str(input("Introduce tu edad: "))
            return edad
        except ValueError:
            if edad.find(".") == True:
                print("**ERROR** La edad no puede ser un numero con decimales")
            elif edad.isalpha() == True:
                print("**ERROR** Introduce un numero no una letra.")



def main():
    try:
        edad = pedir_edad()
        for i in range(1, int(edad)+1, +1):
            print(i)
    except:

        return 0

if __name__ == "__main__":
    main()