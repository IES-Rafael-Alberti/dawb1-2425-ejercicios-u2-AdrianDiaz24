# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
# mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def main():
    try:
        num = int(input("Introduce un Nº: "))
        print(f"Introduciste el Nº {num}")
    except ValueError as e:
        print("La entrda no es correcta.")
        raise e

if __name__ == "__main__":
    main()













