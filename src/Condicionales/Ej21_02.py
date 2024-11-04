# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def pedir_contraseña():
    contraseña = str(input("Introduce la contraseña: "))
    contraseña = contraseña.lower()
    return contraseña



def comprobar_contraseña(contraseña, contraseña_s):
    if contraseña_s == contraseña:
        print("La contraseña proporcionada es la correcta.")
    else: 
        print("La contraseña proporcionada es incorrecta.")
    return 0


def main():
    contraseña = str("manolete")
    contraseña_s = pedir_contraseña()
    comprobar_contraseña(contraseña, contraseña_s)
    return 0

if __name__ == "__main__":
    main()