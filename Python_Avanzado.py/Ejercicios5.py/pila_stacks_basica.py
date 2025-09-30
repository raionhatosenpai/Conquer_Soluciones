#  Crea una clase "Pila" que represente una pila (stack) básica. Implementa 
# métodos para agregar elementos a la pila, quitar elementos y mostrar el 
# contenido actual.

class Pila:# Clase que representa una pila (stack) básica
    def __init__(self):
        self.elementos = []
    # Método para agregar un elemento a la pila
    def agregar(self, elemento):
        self.elementos.append(elemento)
        print(f'Elemento {elemento} agregado a la pila.')
    # Método para quitar el elemento superior de la pila
    def quitar(self):
        if not self.esta_vacia():
            elemento = self.elementos.pop()
            print(f'Elemento {elemento} quitado de la pila.')
            return elemento
        else:
            print('La pila está vacía. No se puede quitar ningún elemento.')
            return None
    # Método para mostrar el contenido actual de la pila
    def mostrar(self):
        if not self.esta_vacia():
            print('Contenido actual de la pila:', self.elementos)
        else:
            print('La pila está vacía.')
    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.elementos) == 0
    
# Ejemplo de uso, primero se crea una instancia de la clase Pila y luego se
# llaman a sus métodos para demostrar su funcionalidad.
pila = Pila()
pila.mostrar()# Muestra que la pila está vacía, no es necesario, me gusta más así
# Agrega varios elementos a la pila y muestra su contenido después de cada operación
pila.agregar("primera")
pila.mostrar()
pila.agregar("segunda")
pila.mostrar()
pila.agregar("tercera")
pila.mostrar()
pila.agregar("cuarta")
pila.mostrar()
pila.agregar("quinta")
pila.mostrar()
# Quita varios elementos de la pila y muestra su contenido después de cada operación
pila.quitar()
pila.mostrar()
pila.quitar()
pila.mostrar()
pila.quitar()
pila.mostrar()
pila.quitar()
pila.mostrar()
pila.quitar()
pila.mostrar()
pila.quitar()  # Intento de quitar de una pila vacía