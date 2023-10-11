# Variables dimensionadas para almacenar datos de pasajeros, ciudades, y socios del club
passengers = []  # Lista para almacenar datos de pasajeros
cities = []      # Lista para almacenar datos de ciudades
members = {}     # Diccionario para almacenar datos de los miembros del club

# Función para agregar un pasajero a la lista de viajeros
def add_passenger(name, dni, destination):
    passengers.append([name, dni, destination])

# Función para agregar una ciudad a la lista de ciudades
def add_city(city, country):
    cities.append([city, country])

# Función para obtener la ciudad de un pasajero por DNI
def get_city_by_dni(dni):
    for passenger in passengers:
        if passenger[1] == dni:
            return passenger[2]
    return "Pasajero con ese DNI no encontrado."

# Función para contar la cantidad de pasajeros que viajan a una ciudad
def count_passengers_by_city(city):
    return sum(1 for passenger in passengers if passenger[2] == city)

# Función para obtener el país de un pasajero por DNI
def get_country_by_dni(dni):
    for passenger in passengers:
        if passenger[1] == dni:
            for city in cities:
                if city[0] == passenger[2]:
                    return city[1]
    return "Pasajero con ese DNI no encontrado."

# Función para contar la cantidad de pasajeros que viajan a un país
def count_passengers_by_country(country):
    return sum(1 for passenger in passengers if get_country_by_dni(passenger[1]) == country)

# Funcion para registrar a un nuevo miembro del club
def register_member(number, name, last_name, entry_date, dues_up_to_date):
    members[number] = {'name': name, 'last_name': last_name, 'entry_date': entry_date, 'dues_up_to_date': dues_up_to_date}

# Funcion para contar la cantidad de socios del club
def count_members():
    return len(members)

# funcion para registrar que un miembro ha pagado todas las cuotas adeudadas
def pay_dues(number):
    if number in members:
        members[number]['dues_up_to_date'] = True
        print(f"Miembro {number} ha pagado todas las cuotas adeudadas.")
    else:
        print("Miembro no encontrado.")

# Función para imprimir la lista completa de miembros del club
def print_member_list():
    for number, member_data in members.items():
        dues_status = "al día" if member_data['dues_up_to_date'] else "adeudada"
        print(f"Miembro n°{number}, {member_data['name']} {member_data['last_name']}, se unió en: {member_data['entry_date']}, cuota {dues_status}.")

# Función para validar que el DNI tiene 7 u 8 caracteres
def validar_dni(dni):
    return len(dni) in [7, 8]

# Menú
while True:
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Obtener ciudad por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Obtener país por DNI")
    print("6. Contar pasajeros por país")
    print("7. Registrar miembro")
    print("8. Contar miembros del club")
    print("9. Registrar pago de cuotas de miembro")
    print("10. Imprimir lista de miembros")
    print("11. Salir")

    eleccion = input("Elija una opción: ")

    if eleccion == "1":
        nombre, dni, destino = input("Ingrese el nombre, DNI y destino del pasajero separados por espacios: ").split()
        if validar_dni(dni):
            dni = int(dni)
            add_passenger(nombre, dni, destino)
        else:
            print("El DNI debe tener 7 u 8 caracteres.")
        
    elif eleccion == "2":
        ciudad = input("Nombre de la ciudad: ")
        pais = input("País de la ciudad: ")
        add_city(ciudad, pais)
    elif eleccion == "3":
        dni = int(input("Ingrese el DNI del pasajero: "))
        print(f"El pasajero viaja a: {get_city_by_dni(dni)}")
    elif eleccion == "4":
        ciudad = input("Ingrese el nombre de la ciudad: ")
        print(f"La cantidad de pasajeros que viajan a {ciudad} es: {count_passengers_by_city(ciudad)}")
    elif eleccion == "5":
        dni = int(input("Ingrese el DNI del pasajero: "))
        print(f"El pasajero viaja a: {get_country_by_dni(dni)}")
    elif eleccion == "6":
        pais = input("Ingrese el nombre del país: ")
        print(f"La cantidad de pasajeros que viajan a {pais} es: {count_passengers_by_country(pais)}")
    elif eleccion == "7":
        numero_miembro = int(input("Número del miembro: "))
        nombre = input("Nombre del miembro: ")
        apellido = input("Apellido del miembro: ")
        fecha_ingreso = input("Fecha de ingreso del miembro (ddmmaaaa): ")
        cuota_al_dia = input("¿Cuota al día? (s/n): ").lower() == "s"
        register_member(numero_miembro, nombre, apellido, fecha_ingreso, cuota_al_dia)
    elif eleccion == "8":
        print(f"El club tiene {count_members()} miembros.")
    elif eleccion == "9":
        numero_miembro = int(input("Número de miembro que pagó las cuotas: "))
        pay_dues(numero_miembro)
    elif eleccion == "10":
        print_member_list()
    elif eleccion == "11":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
