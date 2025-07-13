# Recibir un input() del usuario y recorrer cada carácter de la cadena, si el carácter es una letra ( usando isalpha() para comprobarlo )
# Si es mayúscula, trabaja con el rango de 65 a 90 (A-Z) y si es minúscula, trabaja con el rango de 97 a 122 (a-z).
# Desplaza cada letra 13 posiciones convirtiéndola a su código ASCII con ord() y luego a su carácter con chr().
# Resta el código base (ord('A') o ord('a')) y suma 13, luego usa el módulo 26 (%26) para asegurarte de que el desplazamiento se mantenga dentro del rango de letras.
# Si el carácter no es una letra, simplemente lo deja sin cambios.
# Junta el resultado en una nueva cadena y la devuelve.

def encriptar_rot13(texto):
    resultado = []
    for char in texto:
        if char.isalpha():  # Verifica si el carácter es una letra
            base = ord('A') if char.isupper() else ord('a')
            desplazamiento = (ord(char) - base + 13) % 26 + base
            resultado.append(chr(desplazamiento))
        else:
            resultado.append(char)  # Deja los caracteres no alfabéticos sin cambios
    return ''.join(resultado)

# Ejemplo de uso, permitiendo añadir mas de una cadena de texto
if __name__ == "__main__":
    texto1 = input("\nIntroduce texto (1) a encriptar con ROT13: ")
    texto2 = input("\nIntroduce texto (2) a encriptar con ROT13: ")
    texto_encriptado1 = encriptar_rot13(texto1)
    texto_encriptado2 = encriptar_rot13(texto2)

    print(f"\nTexto encriptado (1): {texto_encriptado1}")
    print(f"\nTexto encriptado (2): {texto_encriptado2}")

    if (texto_encriptado1) == (texto_encriptado2):
        print("\nLos textos encriptados son iguales.")
    else:
        print("\nLos textos encriptados son diferentes.")
