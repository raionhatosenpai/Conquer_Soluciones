# Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de 
# gatos en el primer archivo y tres nombres de perros en el segundo archivo. 
# Escribe un programa que intente leer estos archivos e imprima el contenido 
# de cada archivo en la pantalla. Envuelve tu código en un bloque try-except 
# para capturar el error de FileNotFoundError, e imprime un mensaje amigable 
# si falta algún archivo. Mueve uno de los archivos a una ubicación diferente 
# en tu sistema y asegúrate de que el código en el bloque except se ejecute 
# correctamente. Modifica tu bloque except para que falle en silencio si falta 
# alguno de los archivos.

def leer_archivos(filenames):
    """Leer archivos y manejar FileNotFoundError"""
    try:
        with open(filenames) as file:
            contenido = file.read()
    except FileNotFoundError:
        # Mostrar mensaje amigable si el archivo no se encuentra
        msg = f"\nLo siento, el archivo " + filenames + " no se encuentra."
        print(msg)
        # Para fallar en silencio: descomenta la línea siguiente y comenta las de arriba
        # pass
    else:
        # Imprimir contenido del archivo
        print(f"\nContenido del archivo '{filenames}':\n{contenido}")

# Lista de archivos a leer
filenames = ['cats.txt', 'fish.txt', 'dogs.txt']

for filename in filenames:
    leer_archivos(filename)
