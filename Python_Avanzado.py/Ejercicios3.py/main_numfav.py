#  Escribe un programa separado que lea este valor e imprima el mensaje:
#  "Sé cuál es tu número favorito… Es ____.”

# Importa las funciones del otro archivo
from numero_favorito import leer_numero_favorito, guardar_numero_favorito

# Crea una función principal para manejar la lógica del programa
def main():
    numero_favorito = leer_numero_favorito()
    
    if numero_favorito is not None:
        print(f"Sé cuál es tu número favorito… Es {numero_favorito}.")
    else:
        numero_favorito = input("¿Cuál es tu número favorito? ")
        guardar_numero_favorito(numero_favorito)

# Ejecuta la función principal
if __name__ == "__main__":
    main()