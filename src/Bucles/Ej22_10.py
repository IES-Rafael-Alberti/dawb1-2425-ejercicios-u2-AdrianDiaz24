# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
# número primo o no.


def pedir_num():
    num = int(input("Introduce un Nº entero: "))
    return num


def comprobar_primo(num):
    a = 0
    if num == 1:
        primo = "es primo"
        return primo
    else:
        for i in range(1, num+1, +1):
            if num%i == 0:
                a = a+1
            else:
                a = a
        if a == 2:
            primo = "es primo"        
        else:
            primo = "no es primo"
        return primo


def main():
    num = pedir_num()
    primo = comprobar_primo(num)
    print(f"El {num} {primo}.")
    return 0

if __name__ == "__main__":
    main()