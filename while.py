""" Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
par=int(0)
impar=int(0)
numero=int(1) #declaro la variable numero y la inicializo en 1 para que el bucle while pueda iniciar y que pueda tener como condicion de salida el numero 0
while numero>0:
    numero=int(input("ingrese un numero entero positivo: "))
    if numero>0:
        if numero%2==0: #calculo con la operacion de modulo para saber si es par
            par = par+1
        else: impar = impar+1
    else: print("el numero ingresado es negativo")
    if numero == 0:
        print("la cantidad de numeros pares ingresados es: ",par)
        print("la cantidad de numeros impares ingresados es: ",impar)
    pass
pass