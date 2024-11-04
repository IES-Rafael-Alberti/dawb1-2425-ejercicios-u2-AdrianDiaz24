# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def main():
    for i in range(1, 11, +1):
        print(f"\nTABLA DE MULTIPLIAR DEL {i}")
        for a in range(1, 11, +1):
            tabla =    tabla = f"- {i} X {a} = {i*a}" 
            print(tabla)
    return 0

if __name__ == "__main__":
    main()