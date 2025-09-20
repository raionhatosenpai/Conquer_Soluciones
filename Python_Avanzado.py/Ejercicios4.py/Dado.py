# Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras. 
# Implementa un método para lanzar el dado y mostrar el resultado 
# (quizás te convenga usar el modulo random).

# importamos el módulo random para generar números aleatorios
import random

# definimos la clase Dado
class Dado:
    def __init__(self):
        # el dado tiene 6 caras
        self.caras = 6

    def lanzar(self):
        # generamos un número aleatorio entre 1 y 6
        resultado = random.randint(1, self.caras)
        return resultado
    
# ejemplo de uso
if __name__ == "__main__":
    dado = Dado()
    while True:
        input("Presiona ENTER para lanzar el dado (o escribe 'salir' para terminar): ")
        resultado = dado.lanzar()
        print(f"🎲 Resultado: {resultado}\n")

        continuar = input("¿Quieres lanzar de nuevo? (s/n): ").strip().lower()
        if continuar != "s":
            print("¡Hasta la próxima!")
            break