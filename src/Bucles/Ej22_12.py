# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de 
# veces que aparece la letra en la frase.


def pedir_frase():
    frase = str(input("Introduce una frase: "))
    return frase


def pedir_letra():
    letra = str(input("Introduce una letra: "))
    return letra


def main():
    frase = pedir_frase()
    letra = pedir_letra()
    frase = frase.lower()
    letra = letra.lower()
    a = frase.count(letra)
    print(f"La letra {letra.upper()} aparece {a} veces")
    return 0

if __name__ == "__main__":
    main()