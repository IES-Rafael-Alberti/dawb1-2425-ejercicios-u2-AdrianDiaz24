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
    return letra


def main():
    frase = str(input("Introduce una frase: "))
    letra =  pedir_letra()
    
    return 0

if __name__ == "__main__":
    main()