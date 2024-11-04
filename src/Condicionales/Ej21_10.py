# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def pedir_tipo():
    tipo = str(input("Introduzca el tipo de pizza que desea (Introduzca el Nº): \n1. -> Vegetariana \n2. -> No vegetariana\n\n-> "))
    while not tipo == "1" and not tipo == "2":
        tipo = str(input("**ERROR** Valor invalido, Introduzca el Nº correspondiente al tipo de pizza que desea: \n1. -> Vegetariana \n2. -> No vegetariana\n\n-> "))
    return tipo


def pedir_ingrediente(tipo):
    if tipo == "1":
        ingrediente = str(input("Haz elegido una pizza vegetariana, elige un ingrediente que añadir: \n Ingredientres basicos (No elegibles):\n -> Mozzarella\n -> Tomate\n\n Ingredientes a elegir (solo uno): \n -> 1. Pimiento \n -> 2. Tofu \n\n -> "))
        while not ingrediente == "1" and not ingrediente == "2":
            ingrediente = str(input("**ERROR** Valor invalido, Introduzca el Nº del ingrediente: \n Ingredientes a elegir (solo uno): \n -> 1. Pimiento \n -> 2. Tofu \n\n -> "))
    else:
        ingrediente = str(input("Haz elegido una pizza no vegetariana, elige un ingrediente que añadir: \n Ingredientres basicos (No elegibles):\n -> Mozzarella\n -> Tomate\n\n Ingredientes a elegir (solo uno): \n -> 1. Peperoni \n -> 2. Jamon \n -> 3. Salmon  \n\n -> "))
        while not ingrediente == "1" and not ingrediente == "2" and not ingrediente == "3":
            ingrediente = str(input("**ERROR** Valor invalido, Introduzca el Nº del ingrediente: \n Ingredientes a elegir (solo uno):\n -> 1. Peperoni \n -> 2. Jamon \n -> 3. Salmon  \n\n ->"))
    return ingrediente


def convertir_t(tipo):
    if tipo == "1":
        tipo_p = "Vegetariana"
    else: 
        tipo_p = "No vegetariana"
    return tipo_p


def convertir_i(ingrediente, tipo):
    if tipo == "1":
        if ingrediente == "1":
            ingrediente = "Pimiento"
        else:
            ingrediente = "Tofu"
    else:
        if ingrediente == "1":
            ingrediente = "Peperoni"
        elif ingrediente == "2":
            ingrediente = "Jamom"
        else:
            ingrediente = "Salmon"
    return ingrediente


def main():
    tipo_p = pedir_tipo()
    ingrediente = pedir_ingrediente(tipo_p)
    ingrediente = convertir_i(ingrediente, tipo_p)
    tipo_p = convertir_t(tipo_p)

    print(f"\nSu pizza:\n -> {tipo_p}\nIngredientes:\n -> Mozzarella\n -> Tomate\n -> {ingrediente}")
    
    return 0

if __name__ == "__main__" :
    main()