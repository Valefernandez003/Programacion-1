"""1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
La función debe devolver el tiempo que tarda la rata en salir de la jaula."""
import random
def exit_time():
    n=random.randint(1,3)
    if n == 3:
        return 7
    elif n == 1:
        return 3+exit_time()
    elif n ==2:
        return 5 + exit_time()
print (exit_time())

"""2. Escribir una consigna apropiada para la siguiente función. Asumir que n es un número
entero."""
def f(n):
    s=str(n) #transforma la variable n que es un entero en un string
    if len(s) <= 1: #si es un solo numero devuelve ese valor
        return s
    return s[-1] + f(int(s[:-1])) #retornamos la ultima posicion y llamamos de forma recurisva la variable restandalo un valor y transformandolo en entero