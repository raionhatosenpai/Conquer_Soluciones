# Averigua cuántas veces aparece una palabra o frase en el texto (puedes usar el método count()).

# Función para contar palabras en un texto
def contar_palabras(textos, palabra):
  """Contar cuántas veces aparece una palabra en un texto."""
  with open(textos, encoding="utf-8") as archivos:  # Usa utf-8 o cambia a utf-16 si da error
    contenido = archivos.read().lower()  # Leer y convertir a minúsculas
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    contador = contenido.count(palabra)  # Contar ocurrencias
    print(f"La palabra '{palabra}' aparece {contador} veces en el texto.")

# Nombre del archivo de texto
textos = ("Gabriel_Garcia.txt", "Miguel_Cervantes.txt", "Chat_Gpt.txt")

# Solicitar al usuario la palabra a buscar en cada texto
for texto in textos:
 palabra = input(f"\nIngrese la palabra que desea buscar en {texto}: ")
 contar_palabras(texto, palabra)

 # aqui se debe estqr en la misma carpeta/ruta que el archivo de texto