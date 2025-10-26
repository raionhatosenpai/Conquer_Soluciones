import string

# Caché global para memoización
memo = {}

def calcular_frecuencia_palabras(texto, memo=None):
    if memo is None:
        memo = {}

    # Verificar si el resultado ya está en la memoria caché
    if texto in memo:
        print("🔁 Recuperando del caché...")
        return memo[texto]

    # Convertir a minúsculas y eliminar signos de puntuación
    texto_limpio = texto.lower().translate(str.maketrans('', '', string.punctuation))
    palabras = texto_limpio.split()

    # Lista de palabras comunes (stopwords)
    palabras_comunes = {
        "el", "la", "los", "las", "un", "una", "unos", "unas",
        "y", "o", "de", "del", "a", "en", "con", "por", "para", "es", "que",
        "se", "no", "al", "lo", "su", "sus", "mi", "mis", "tu", "tus", "me", "te",
        "le", "les", "nos", "como", "ya", "pero", "más", "si", "esto", "eso"
    }

    frecuencia = {}
    for palabra in palabras:
        if palabra not in palabras_comunes:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    # Guardar en caché
    memo[texto] = frecuencia
    return frecuencia

# Bucle de análisis interactivo
while True:
    texto = input("\n📥 Introduce un texto para analizar (o 'salir' para terminar): ")
    if texto.lower() == 'salir':
        print("👋 Saliendo del programa.")
        break

    frecuencia_palabras = calcular_frecuencia_palabras(texto, memo)

    print("\n📊 Frecuencia de palabras relevantes:")
    if frecuencia_palabras:
        for palabra, freq in sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True):
            print(f"🔹 {palabra}: {freq}")
    else:
        print("⚠️ No se encontraron palabras significativas en el texto.")
