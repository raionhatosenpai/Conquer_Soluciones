# Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa 
# un método para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return self.longitud * self.ancho

    def perimetro(self):
        return 2 * (self.longitud + self.ancho)
    
# Solicitar datos al usuario
while True:
 try:
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    break
 except ValueError:
    print("Por favor, ingresa solo valores numéricos.")
 
# Crear un objeto de la clase Rectangulo
rectangulo = Rectangulo(longitud, ancho)
print(f"\n Área del rectángulo: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")