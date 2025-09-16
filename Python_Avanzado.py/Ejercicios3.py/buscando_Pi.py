# Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi
# (y en que posición. Puedes usar find()). 
# Puedes usar el archivo pi_10000.txt

# Función para buscar una cadena en los primeros 10000 dígitos de pi
def buscar_en_pi(documento, cadena):
    """Buscar una cadena en los primeros 10000 dígitos de pi."""
    with open("pi_10000.txt") as archivo:  # Abrir el archivo pi_10000.txt
        pi_digitos = archivo.read()  # Leer el contenido del archivo
        posicion = pi_digitos.find(cadena)  # Buscar la posición de la cadena
        if posicion != -1:
         print(f"La cadena '{cadena}' se encuentra en la posición {posicion} de los primeros 10000 dígitos de pi.")
        else:
         print(f"La cadena '{cadena}' no se encuentra en los primeros 10000 dígitos de pi.")

# archivo pi_10000.txt debe estar en la misma carpeta/ruta que este script
documento = ("pi_10000.txt")

# Solicitar al usuario la cadena a buscar
cadena = input("Ingrese la fecha de su aniversario: ")
buscar_en_pi(documento, cadena)