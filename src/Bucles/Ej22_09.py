# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def comprobar_contraseña(contraseña):
    contraseña_i = str(input("Introduce la contraseña: "))
    while contraseña_i != contraseña:
        contraseña_i = str(input("**Contraseña erronea** Introduce la contraseña: "))
    return contraseña

def main():
    contraseña = "contraseña"
    comprobar_contraseña(contraseña)
    return 0

if __name__ == "__main__":
    main()