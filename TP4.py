"""1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x."""
x=0
while x < 30:
    x=x+1
    if x == 4:
        print("the value ", str(x), "of x was skipped")
        x==x+1
        continue
    if x == 6:
        print("the value ", str(x), "of x was skipped")
        x==x+1
        continue
    if x == 10:
        print("the value ", str(x), "of x was skipped")
        x==x+1
        continue
    print( "the value of the loop is: " + str(x))
    if x==15:
        print("The execution of the loop was broken when x was ", str(x))
        break

"""1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas."""
while True:
    line=input("ingrese la linea que quiere convertir a mayusculas (deje en blanco si desea finalizar): ")
    if not line: 
        break
    upper_line = line.upper()
    print(upper_line)
print("usted ha salido")

"""2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350"""
cash = 0
opregister=[]
while True:
    operation=input("indique que operacion desea realizar D para depositar o R para retirar, deje en blanco para finalizar: ")
    if not operation:
        break
    upperoperation=operation.upper()
    if upperoperation not in ["D","R"]:
        print("ERROR")
        continue
    try:
        amount=float(input("ingrese el monto que quiere operar: "))
    except ValueError:
        print("monto no válido")
        continue
    if upperoperation=="D":
        cash+=amount
    elif upperoperation=="R":
        if cash >= amount:
            cash -= amount
        else:
            print("saldo insuficiente")
            continue
    opregister.append(f"{operation} {amount}")
print("el saldo final es: ",cash)
print("Bitácora de operaciones:")
for registro in opregister:
    print(registro)
pass

"""3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados."""
primecount=0
primeregister=[]

while True:
    num=int(input("ingrese numeros mayores que 1, para finalizar ingrese 0: "))
    if num <= 1:
        break
    else: 
        is_prime = True #creo una variable booleana que sea verdadera por defecto
        for i in range(2,num):
            if num%i==0:
                is_prime=False # la variable se va a convertir en falsa si en algun valor del recorrido alguna de los modulos da 0
        if is_prime:
            primecount+=1
print("la cantidad de numeros primos ingresados es: ",primecount)

"""4-Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
que sean bisiestos y múltiplos de 10. Nota: Para que un año sea bisiesto debe ser divisible por 4 y 
no debe ser divisible por 100, excepto que también sea divisible por 400."""

# Solicitamos al usuario que ingrese el año de inicio y fin del rango.
starting_year = int(input("Ingrese el año de inicio: "))
end_year = int(input("Ingrese el año de fin: "))

# Iniciamos un bucle que recorre todos los años en el rango especificado.
for year in range(starting_year, end_year + 1):
    # Verificamos si el año es bisiesto y múltiplo de 10.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            # Si cumple ambas condiciones, lo imprimimos.
            print(year)

# Informamos al usuario que hemos terminado de imprimir los años.
print("Fin del programa")

"""5-Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
Utiliza la declaración continue para omitir los números impares."""

# Iniciamos un bucle for que recorre números del 1 al 20 (inclusive).
for number in range(1, 21):
    # Verificamos si el número es impar.
    if number % 2 != 0:
        # Si es impar, usamos 'continue' para omitirlo y pasar al siguiente número.
        continue
    # Si llegamos aquí, el número es par y lo imprimimos.
    print(number)

# Informamos al usuario que hemos terminado de imprimir los números pares.
print("Fin del programa")

"""6-Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
Cuando encuentres el número, usa break para salir del bucle."""

# Creamos una lista de números.
numbers = [10, 25, 5, 45, 15, 30, 35]

# Definimos el número que queremos encontrar.
search_number = 30

# Iniciamos un bucle for para recorrer la lista de números.
for number in numbers:
    # Verificamos si el número actual es igual al número que queremos encontrar.
    if number == search_number:
        # Si encontramos el número, usamos 'break' para salir del bucle.
        print(f"¡Encontramos el número {search_number}!")
        break

# Si llegamos aquí y no se encontró el número, informamos al usuario.
else:
    print(f"El número {search_number} no se encontró en la lista.")

# Informamos al usuario que hemos terminado de buscar.
print("Fin del programa")

"""7-Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while 
para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle 
(Mostrar un mensaje por cada opción elegida)."""

# Definimos una función para mostrar el menú de opciones.
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

# Iniciamos un bucle while para mostrar el menú y permitir que el usuario seleccione una opción.
while True:
    # Mostramos el menú de opciones.
    mostrar_menu()
    
    # Solicitamos al usuario que ingrese una opción.
    option = input("Seleccione una opción (1/2/3/0): ")
    
    # Verificamos la opción ingresada por el usuario.
    if option == "1":
        print("Ha seleccionado la Opción 1.")
    elif option == "2":
        print("Ha seleccionado la Opción 2.")
    elif option == "3":
        print("Ha seleccionado la Opción 3.")
    elif option == "0":
        print("Saliendo del programa...")
        break  # Salimos del bucle si el usuario ingresa "0".
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Informamos al usuario que hemos terminado el programa.
print("Fin del programa")

    
