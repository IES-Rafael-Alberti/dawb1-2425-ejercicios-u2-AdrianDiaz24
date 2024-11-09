# Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. 
# Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y 
# entiendes su funcionamiento.


def ordenar_lista(lista):
    """_summary_

    Args:
        lista (list): La lista escrita por el usuario con el orden original

    Returns:
        list: La lista ordenada de menor a mayor
    """
    i = 0
    b = len(lista)
    for i in range(0, b-1-i, +1):
        for j in range(0, b-1-i, +1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def pedir_lista():
    """Esto te pide 10 numeros para ingresarlo a la lista que hay que ordenar

    Returns:
        list: Te devuelve la lista introducida por el usuario sin ordenar
    """
    lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 10, +1):
        num = int(input(f"Introduce el Nº {i+1} de 10: "))
        lista[i] = num

    return lista


def main():

    lista = pedir_lista()
    print(f"\nLa lista desordenada es {lista}\n")
    lista = ordenar_lista(lista)
    print(f"La lista ordenada es {lista}")
    return

if __name__ == "__main__":
    main()






