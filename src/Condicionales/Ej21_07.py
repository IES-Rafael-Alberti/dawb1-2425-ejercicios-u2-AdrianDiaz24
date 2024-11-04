# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
# < 10.000 = 5%, >= 10.000 or <20.000 = 15%, >= 20.000 or <35.000 = 20%, >= 35.000 or <60.000 = 30%, <60.000 = 45%,


def pedir_renta():
    renta = float(input("Introduce tu renta anual: "))
    renta = round(renta, 2)
    while renta < 0:
        renta = float(input("**ERROR** Valor invalido introduce uno valido: "))
    return renta


def calcular_impositivo(renta):
    if renta < 10000:
        impositivo = "5%"
    elif renta >= 10000 and renta < 20000:
        impositivo = "15%"
    elif renta >= 20000 and renta < 35000:
        impositivo = "20%"
    elif renta >= 35000 and renta < 60000:
        impositivo = "30%"
    else:
        impositivo = "45%"
    return impositivo


def main():
    renta = pedir_renta()
    impositivo = calcular_impositivo(renta)

    print(f"Su renta es de {renta}€ por lo cual su tipo impositivo es del {impositivo}")

    return 0

if __name__ == "__main__":
    main()