# Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
# lance la excepción NameError con el mensaje, "Incorrect Password!!"



def main():
    contraseña_c = "manolo"
    contraseña = str(input("Introduce la contraseña: "))
    if contraseña_c != contraseña:
        raise NameError("Incorrect Password!!")
    else:
        print("Contraseña correcta")
    return

if __name__ == "__main__":
    main()




