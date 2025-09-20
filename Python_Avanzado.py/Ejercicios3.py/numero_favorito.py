# Escribe un programa que solicite al usuario su número favorito.
# Utiliza json.dump() para almacenar este número en un archivo.

# Importa los módulos necesarios
import json # Manejar datos JSON

# Define la ruta del archivo
file_path = 'numero_favorito.json' # Asegúrate de que el directorio existe

# Crea una función para leer el número favorito desde el archivo
def leer_numero_favorito():
    try:
        with open(file_path, 'r') as file: # Abre el archivo en modo lectura
            num = json.load(file)
            return num
    except FileNotFoundError:# Si el archivo no existe
        return None
    except json.JSONDecodeError: # Si el archivo está vacío o corrupto
        return None
    
# Crea una función para guardar el número favorito en el archivo
def guardar_numero_favorito(num):
    with open(file_path, 'w') as file: # Abre el archivo en modo escritura
        json.dump(num, file)