# Crea una clase "Coche" con atributos como marca, modelo y año. 
# Implementa un método para encender el coche y otro para apagarlo 
# (puedes simular el encendido y apagado con una variable booleana)

# Clase Coche
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Estado del coche (encendido o apagado)

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El coche {self.marca} {self.modelo} del {self.año} ha sido encendido.")
        else:
            print(f"El coche {self.marca} {self.modelo} del {self.año} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El coche {self.marca} {self.modelo} del {self.año} ha sido apagado.")
        else:
            print(f"El coche {self.marca} {self.modelo} del {self.año} ya está apagado.")

# Ejemplo de uso
while True:
    try:
     marca = input("Ingrese la marca del coche: ").title()
     modelo = input("Ingrese el modelo del coche: ").title()
     año = int(input("Ingrese el año del coche: "))
    except ValueError:
     print("Por favor, ingrese un año válido (número entero).")

    mi_coche = Coche(marca, modelo, año)

    while True:
        accion = input("¿Desea encender (e) o apagar (a) el coche? (s para salir): ").lower()
        if accion == 'e':
            mi_coche.encender()
        elif accion == 'a':
            mi_coche.apagar()
        elif accion == 's':
            print("Saliendo del programa.")
            exit()
        else:
            print("Acción no reconocida. Por favor, ingrese 'e', 'a' o 's'.")
# El programa permite crear un coche y encenderlo o apagarlo según la entrada del usuario.