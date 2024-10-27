# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def pedir_tipo():
    tipo = str(input("Introduzca el tipo de pizza que desea (Introduzca el Nº): \n1. -> Vegetariana \n2. -> No vegetariana\n-> "))
    while not tipo == "1" or tipo == "2":
        tipo = str(input("**ERROR** Valor invalido, Introduzca el Nº correspondiente al tipo de pizza que desea: \n1. -> Vegetariana \n2. -> No vegetariana\n-> "))
    return tipo

def main():
    tipo_p = pedir_tipo()
    
    return 0

if __name__ == "__main__" :
    main()