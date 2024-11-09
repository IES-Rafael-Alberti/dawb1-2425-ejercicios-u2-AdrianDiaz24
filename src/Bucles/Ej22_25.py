# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: 
# se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.


def comprobar_palabras(frase:str):
    frase = frase.split(" ")
    contador = 0
    for palabra in frase:
        a = len(palabra)
        if a > contador:
            palabra_larga = palabra
            contador = a
    return palabra_larga


def comprobar_num_palabras(frase):
    frase = frase.split(" ")
    num_palabras = 0
    for palabra in frase:
        num_palabras += 1
    return num_palabras


def main():
    frase = str(input("Introduce una frase: "))
    while frase == "":
        frase = str(input("**ERROR** Campo no rellenado.\nIntroduce una frase: "))
    palabra_larga = comprobar_palabras(frase)
    num_palabras = comprobar_num_palabras(frase)

    print(f"La palabras mas larga es {palabra_larga} y la frase tiene un total de {num_palabras} palabras.")

    return 0

if __name__ == "__main__":
    main()


