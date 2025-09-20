# Define una clase Persona con atributos como nombre, edad y profesión. 
# Luego, crea varios objetos de esta clase y muestra su información.

# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre.title()
        self.edad = edad
        self.profesion = profesion.title()
    def details(self):
        print("--------"*10)
        print("Información de la persona:")
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion}")    

# Solicitar datos al usuario
nombre =  input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
profesion = input("Ingrese la profesión: ")

# Crear un objeto de la clase Persona
info_persona = Persona(nombre, edad, profesion)
info_persona.details()