def main(): 
    try:
        #pedimos al usuario que ingrese la fecha 
        fecha_actual=str(input("Ingrese la fecha en el siguiente formato: Día,DD/MM: "))
        dia_semana, fecha = fecha_actual.split(',') #con un split dividimos la variable fecha actual en dos variables, una para almacenar el dia y otra para almacenar la fecha
        dia, mes = fecha.split('/') #divido la fecha en dos variables, cada una que va a almacenar una parte de la fecha
        dia_semana=dia_semana.lower()
        dia_semana_valido=["lunes","martes","miercoles","jueves","viernes"]

        if dia_semana not in dia_semana_valido or int(dia) > 31 or int(mes) > 12:  #condiciones para que salga un mensaje de error
         print("Error, un dato ingresado es incorrecto")
         return
        #segun caso con los dias de la semana
        if dia_semana == "lunes":
            procesar_examen()
        elif dia_semana== "martes":
           procesar_examen()
        elif dia_semana=="miercoles":
           procesar_examen()
        elif dia_semana== "jueves":
           practica_hablada()
        elif dia_semana== "viernes":
           ingles_viajero(dia,mes)  
    except ValueError:  
        print("ocurrió un error")
def procesar_examen(): #funcion que saque el porcentaje de alumnos aprobados
    alumnos = int(input("ingrese la cantidad de alumnos del curso "))
    aprobados=int(input("ingrese la cantidad de alumnos aprobados "))
    porcentaje = (aprobados/alumnos)*100
    print(f"el porcentaje de alumnos aprobados es: {porcentaje}%")
def practica_hablada(): #funcion que dice si fue mas de el 50% de la clase
    asistencia= float(input("ingrese el porcentaje de asistencia sin '%': "))
    if asistencia > 50:  
        print("asistió la mayoría")
    else:
        print("faltó la mayoría")
def ingles_viajero(dia,mes): #funcion que saca el total de los aranceles
    arancel=float(input("ingrese el arancel por alumno: "))
    alumnos= int(input("ingrese la cantidad de alumnos: "))
    if (dia==1 and mes==1) or (dia==1 and mes==7):
      print("comienzo de un nuevo ciclo")
    pass
    print("el ingreso total sera de: ", arancel*alumnos,"$")
if __name__ == "__main__":
        main()
