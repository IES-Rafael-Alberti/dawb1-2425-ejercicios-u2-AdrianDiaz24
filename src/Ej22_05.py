# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
# dura la inversión.


def pedir_inversion():
    inversion = float(input("Introduce la cantidad que desea invertir: "))
    while inversion < 0:
        inversion = float(input("**ERROR** Valor invalido, introduce uno valido: "))
    return inversion


def pedir_interes():
    interes = float(input("Introduce el interes anual de su inversion: "))
    while interes < 0:
        interes = float(input("**ERROR** Valor invalido, introduce uno valido: "))
    return interes


def pedir_años():
    años = int(input("Introduce la cantidad que desea invertir: "))
    while años < 0:
        años = int(input("**ERROR** Valor invalido, introduce uno valido: "))
    return años


def calcular_capital_o(inversion, interes, año):
    i = 0
    while i < año:
        capital_o = (inversion*(1+(interes/100)))
        inversion = inversion + capital_o
    return capital_o


def main():
    inversion = pedir_inversion()
    interes = pedir_interes()
    años = pedir_años()

    for año in range(0, años, +1):
        capital_o = calcular_capital_o(inversion, interes, año)

        print(f"El {año}º año obtendras un capital de {capital_o}€")

    return 0

if __name__ == "__main__":
    main()