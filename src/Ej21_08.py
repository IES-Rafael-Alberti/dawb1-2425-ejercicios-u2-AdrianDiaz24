# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
# Inaceptable	0.0, Aceptable	0.4, Meritorio	0.6 o más
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

def pedir_puntuacion():
    puntuacion = float(input("Introduzaca su puntuacion (0.0, 0.4, 0.6 o mas): "))
    while puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
        return puntuacion
    print("**ERROR** Valor invalido")


def comprobar_puntuacion(puntuacion):
    if puntuacion == None:
        puntuacion = pedir_puntuacion()
    return puntuacion


def comprobar_rendimiento(puntuacion):
    if puntuacion == 0.0:
        rendimiento = "Inaceptable"
    elif puntuacion == 0.4:
        rendimiento = "Aceptable"
    else:
        rendimiento = "Meritorio" 
    return rendimiento


def main():
    puntuacion = pedir_puntuacion()
    puntuacion = comprobar_puntuacion(puntuacion)
    rendimiento = comprobar_rendimiento(puntuacion)
    print (rendimiento)
    return 0

if __name__ == "__main__":
    main()