# Lista de de caracteres llamada “palabras“ que representa una mano de Scrabble.
palabras = { 'A': 5, 'E': 4, 'I': 3, 'O': 2, 'U': 1, 'B': 6, 'C': 5, 'D': 4, 'F': 3, 
             'G': 2, 'H': 1, 'J': 8, 'K': 7, 'L': 6, 'M': 5, 'N': 4, 'P': 3, 'Q': 10, 'R': 2, 
                 'S': 1, 'T': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

# Crear una variable 'total_puntos' inicializada en 0. Esta almacenará la suma total de los puntos.
total_puntos = 0

palabra_scrabble = input("Introduce la palabra de Scrabble: ").upper()
# Iterar sobre cada letra en la palabra ingresada.
for letra in palabra_scrabble:
    # Si la letra está en el diccionario 'palabras', sumar su valor al total de puntos.
    if letra in palabras:
        total_puntos += palabras[letra]
        print(f"{letra}: {palabras[letra]} puntos")
    # Si la letra no está en el diccionario, imprimir un mensaje de advertencia.
    else:
        print(f"La letra '{letra}' no es válida en Scrabble.")

# Imprimir el total de puntos obtenidos.
print("Total de puntos obtenidos:", total_puntos)