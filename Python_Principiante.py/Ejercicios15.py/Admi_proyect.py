# Eres un gerente de proyectos y necesitas un programa para administrar
# las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
# una descripción y un responsable asignado. Implementa un programa en
# Python que utilice un diccionario para almacenar la información de las
# tareas. El programa debe permitir agregar nuevas tareas, asignar
# responsables a las tareas existentes, actualizar las descripciones de las
# tareas y mostrar la lista completa de tareas y responsables. 

# (Pista: puedes comenzar con un diccionario vacío y construir un diccionario de diccionarios)

# diccionario {nombre, descripcion, responsable}
tareas = {}

# Función para agregar una nueva tarea
def agregar_tarea(nombre, descripcion, responsable):
    tareas[nombre] = {
        "descripcion": descripcion,
        "responsable": responsable
    }

# Función para asignar un responsable a una tarea existente
def asignar_responsable(nombre, nuevo_responsable):
    if nombre in tareas:
        tareas[nombre]["responsable"] = nuevo_responsable
    else:
        print("La tarea no existe.")

# Función para actualizar la descripción de una tarea existente 
def actualizar_descripcion(nombre, nueva_descripcion):
    if nombre in tareas:
        tareas[nombre]["descripcion"] = nueva_descripcion
    else:
        print("La tarea no existe.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    for nombre, info in tareas.items():
        print(f"Tarea: {nombre}")
        print(f"  Descripción: {info['descripcion']}")
        print(f"  Responsable: {info['responsable']}")

# bucle para interactuar con el usuario
while True:
    nombre_tarea = input("Ingrese el nombre de la tarea (o 'salir' para terminar): ")
    if nombre_tarea.lower() == "salir":
        break

    if nombre_tarea in tareas:
        respuesta = input("Ya existe. ¿Deseas actualizarlo? (s/n): ")
        if respuesta.lower() == "s":
            nueva_descripcion = input("Nueva descripción: ")
            actualizar_descripcion(nombre_tarea, nueva_descripcion)
        nuevo_responsable = input("Nuevo responsable: ")
        asignar_responsable(nombre_tarea, nuevo_responsable)
    else:
        descripcion = input("Descripción de la tarea: ")
        responsable = input("Responsable de la tarea: ")
        agregar_tarea(nombre_tarea, descripcion, responsable)

# Mostrar la lista de tareas
print("\nLista de tareas:")
mostrar_tareas()
print("-" * 30)