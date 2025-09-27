# Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
# Implementa métodos para agregar una tarea, marcar una tarea como 
# completada y mostrar todas las tareas

class ListaTareas:
    def __init__(self):
        self.tareas = []  # Inicializa una lista vacía para las tareas

    def agregar_tarea(self, descripcion):
        self.tareas.append({"descripcion": descripcion, "completada": False})
        print(f"Tarea agregada: '{descripcion}'")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            print(f"Tarea '{self.tareas[indice]['descripcion']}' marcada como completada.")
        else:
            print("Índice de tarea inválido.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")

# Ejemplo de uso
lista = ListaTareas()
while True:
    accion = input("¿Desea agregar (a), marcar completada (m), mostrar tareas (s) o salir (q)? ").lower()
    if accion == 'a':
        descripcion = input("Ingrese la descripción de la tarea: ")
        lista.agregar_tarea(descripcion)
    elif accion == 'm':
        try:
            indice = int(input("Ingrese el índice de la tarea a marcar como completada (0/1/2/3...): "))
            lista.marcar_completada(indice)
        except ValueError:
            print("Por favor, ingrese un índice válido.")
    elif accion == 's':
        lista.mostrar_tareas()
    elif accion == 'q':
        print("Saliendo del programa.")
        exit()  # Sale del programa
    else:
        print("Acción no reconocida. Por favor, ingrese 'a', 'm', 's' o 'q'.")