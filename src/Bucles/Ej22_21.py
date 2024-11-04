# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
# no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total 
# a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 
# 10% de descuento.


def pedir_precio():
    precio = float(input("Introduce el precio de la compra: "))
    return precio


def main():
    precio_f = 0
    while True:
        precio = pedir_precio()
        if precio < 0:
            continue
        elif precio >= 0:
            if precio == 0:
                if precio_f <= 1000:
                    print(f"Total a pagar: {precio_f}")
                    break
                else: 
                    precio_f = precio_f*0.90
                    print(f"Total a pagar: {precio_f}")
                    break
            else:
                precio_f = precio_f+precio
        

    return 0

if __name__ == "__main__": 
    main()