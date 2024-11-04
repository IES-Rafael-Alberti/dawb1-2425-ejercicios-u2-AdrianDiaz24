# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y 
# los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


def pedir_nombre():
    nombre = str(input("Introduzca su nombre: "))
    nombre = nombre.lower()
    nombre = nombre[0]
    return nombre


def pedir_sexo():
    sexo = str(input(f"Introduzca su sexo: \n-> H para hombre \n-> M para mujer \n-> "))
    sexo = sexo.upper()
    
    return sexo


def comprbar_sexo(sexo):
    if sexo == "H" or sexo == "M":
        return sexo
    else:
        sexo = str(input("**ERROR** Introduzca un valor valido \n-> H para hombre \n-> M para mujer \n-> "))
        sexo = sexo.upper()
        comprbar_sexo(sexo)


def comprobar_grupo(nombre, sexo):
    if nombre < "m" and sexo == "M" or nombre < "n" and sexo == "H":
        grupo = "A"
    else:
        grupo = "B"
    return grupo


def main():
    nombre = pedir_nombre()
    sexo = pedir_sexo()
    sexo = comprbar_sexo(sexo)
    grupo = comprobar_grupo(nombre, sexo)

    print(f"Perteneces al grupo {grupo}")

    return 0

if __name__ =="__main__":
    main()