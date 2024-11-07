# Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. 
# Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y 
# entiendes su funcionamiento.


def main():
    a = [8, 3, 1, 19, 14, 50, 2, 71, 4, 22, 39]
    i = 0
    b = len(a)
    for i in range(0, b-1-i, +1):
        for j in range(0, b-1-i, +1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return

if __name__ == "__main__":
    main()






