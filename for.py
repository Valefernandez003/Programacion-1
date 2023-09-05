corrimiento = int(input("cuantas lugares quiere correr las letras? "))
for i in range(5):
    print("mensaje número:", i + 1)
    mensaje = str(input("ingrese el mensaje que quiere encriptar:"))
    def cifrado_cesar(mensaje,corrimiento):
        resultado = ""
        for letra in mensaje:
            if letra.isalpha():  # Verificar si es una letra
                mayuscula = letra.isupper()
                codigo_letra = ord(letra.upper())
                codigo_desplazado = (codigo_letra - ord('A') + corrimiento) % 26 + ord('A')
                letra_desplazada = chr(codigo_desplazado)
            
                if mayuscula:
                    resultado += letra_desplazada
                else:
                    resultado += letra_desplazada.lower()
            else:
                resultado += letra

        return resultado
    mensaje_cifrado=cifrado_cesar(mensaje,corrimiento)
    print("el mensaje original es: ",mensaje)
    print("el mensaje cifrado es: ",mensaje_cifrado)