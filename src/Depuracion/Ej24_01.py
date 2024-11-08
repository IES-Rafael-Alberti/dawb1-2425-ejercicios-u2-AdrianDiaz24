# Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. 
# Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y 
# entiendes su funcionamiento.


def ordenar_lista(lista):
    """_summary_

    Args:
        lista (array): La lista escrita por el usuario con el orden original

    Returns:
        array: La lista ordenada de menor a mayor
    """
    i = 0
    b = len(lista)
    for i in range(0, b-1-i, +1):
        for j in range(0, b-1-i, +1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def main():
    lista = [8, 3, 1, 19, 14, 50, 2, 71, 4, 22, 39]
    lista = ordenar_lista(lista)
    print(f"La lista ordenada es {lista}")
    return

if __name__ == "__main__":
    main()






