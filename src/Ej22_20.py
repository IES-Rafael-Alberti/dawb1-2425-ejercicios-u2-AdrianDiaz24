# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a 
# carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición 
# (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la 
# ejecución.


def pedir_letra():
    letra = str(input("Introducec una letra: "))
    a = len(letra)
    while a > 1 or letra.isalpha() != True:
        letra = str(input("**ERROR** Introduce solo una letra: "))
        a  = len(letra)
    return letra.lower()


def comprobar_caracter(i:int, frase:str, letra:str):
    if frase.lower()[i] == letra:
        return 1
    else:
        return 0


def main():
    frase = str(input("Introduce una frase: "))
    letra =  pedir_letra()


    a = len(frase)
    for i in range(0, a, +1):
        b = comprobar_caracter(i, frase, letra)
        if b == 1:
            print(f"Se ha enocntrado la letra {letra.upper()} en  el caracter Nº {i+1} de la frase")
            continue
        else:
            print(f"No se ha encontrado la letra {letra.upper()}  en el caracter Nº {i+1} de la frase")

    
    return 0

if __name__ == "__main__":
    main()