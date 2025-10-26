'''Imagina que estás trabajando en un sistema de análisis de texto que requiere 
calcular la frecuencia de ocurrencia de palabras en un conjunto de documentos. 
Implementa una función llamada calcular_frecuencia_palabras que 
tome como entrada un texto y devuelva un diccionario que muestre la 
frecuencia de cada palabra en el texto.

1. La función debe ser capaz de manejar textos y ser insensible a 
mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la 
misma palabra).

2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que 
no aportan información relevante al análisis.

3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el 
mismo texto.'''

def calcular_frecuencia_palabras(texto, memo=None):
    if  memo is None:
        memo = {}
    # Verificar si el resultado ya está en la memoria caché
    if texto in memo:
        print("Recuperando del caché...")
        return memo[texto]
    # Convertir el texto a minúsculas y dividirlo en palabras
    texto = texto.lower()
    palabras = texto.split()
    # Definir una lista de palabras comunes a excluir
    palabras_comunes = {"el", "la", "los", "las", "un", "una", "unos", "unas",
                        "y", "o", "de", "del", "a", "en", "con", "por", "para", "es", "que", "se", "no",
                        "al", "lo", "su", "sus", "mi", "mis", "tu", "tus", "me", "te", "le", "les", "nos"}
    frecuencia = {}
    # Calcular la frecuencia de cada palabra
    for palabra in palabras:
        if palabra not in palabras_comunes:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    # Almacenar el resultado en la memoria caché
    memo[texto] = frecuencia
    return frecuencia

# Ejemplo de uso
while True:
    texto = input("Introduce un texto para analizar (o 'salir' para terminar): ")
    if texto.lower() == 'salir':
        break
    frecuencia_palabras = calcular_frecuencia_palabras(texto)
    print(f"la frecuencia de palabras en el texto que haz introducido es: {frecuencia_palabras}")