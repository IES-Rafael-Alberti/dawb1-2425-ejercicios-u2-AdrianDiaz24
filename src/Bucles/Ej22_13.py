# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


def main():
    frase = ""
    while frase != "salir":  
        frase = str(input("Introduce lo que quieras (salir: para cerrar el programa): "))
        if frase != "salir":
            print(f" -> {frase}")
        else: 
            return 0

if __name__ == "__main__":
    main()