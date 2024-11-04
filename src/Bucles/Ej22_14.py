# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números 
# ingresados.


def main():
    a = 0
    num = int(input("(El 0 muestra la suma de los Nº dados y cierra el programa)\nIntroduce un Nº: "))  
    while num != 0:
        a = a+num
        num = int(input("Introduce un Nº: ")) 
    print(f"La suma de todos los Nº dados es {a}")    
    return 0

if __name__ == "__main__":
    main()