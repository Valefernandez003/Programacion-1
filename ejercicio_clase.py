def main(): 
    try:
        #pedimos al usuario que ingrese la fecha
        fecha_actual = input("Ingrese la fecha en el siguiente formato: Día,DD/MM: ")
        dia_semana, fecha = map(str.strip, fecha_actual.split(','))
        dia, mes = fecha.split('/')
        dia_semana = dia_semana.lower()
        dia_semana_valido = ["lunes", "martes", "miercoles", "jueves", "viernes"]
        #validamos el dia ingresado
        if dia_semana not in dia_semana_valido or int(dia) > 31 or int(mes) > 12:
            print("Error, un dato ingresado es incorrecto")
            return
        #switch case dias de la semana
        if dia_semana == "lunes":
            print("nivel inicial")
            examen = input("se tomó examen?")
            procesar_examen(examen)
        elif dia_semana == "martes":
                print("nivel intermedio")
                examen = str(input("se tomó examen?"))
                procesar_examen(examen)
        elif dia_semana == "miercoles":
                print("nivel avanzado")
                examen = input("se tomó examen?")
                procesar_examen(examen)
        elif dia_semana == "jueves":
                 practica_hablada()
        elif dia_semana == "viernes":
                 ingles_viajero(dia, mes)
    except ValueError:  
        print("Ocurrió un error")
        #funcion que calcule el porcentaje de alumnos aprobados
def procesar_examen(examen):
    if examen == "si":
        alumnos = int(input("Ingrese la cantidad de alumnos del curso: "))
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        porcentaje = (aprobados / alumnos) * 100
        print(f"El porcentaje de alumnos aprobados es: {porcentaje}%")
    pass
        #funcion que calcule la asistencia
def practica_hablada():
    asistencia = float(input("Ingrese el porcentaje de asistencia sin '%': "))
    if asistencia > 50:  
        print("Asistió la mayoría")
    else:
        print("Faltó la mayoría")
        #funcion que calcule los aranceles
def ingles_viajero(dia, mes):
    arancel = float(input("Ingrese el arancel por alumno: "))
    alumnos = int(input("Ingrese la cantidad de alumnos: "))
    if (dia == 1 and mes == 1) or (dia == 1 and mes == 7):
        print("Comienzo de un nuevo ciclo")
    
    print("El ingreso total será de:", arancel * alumnos, "$")

if __name__ == "__main__":
    main()

