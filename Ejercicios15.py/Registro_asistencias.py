# Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
# estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
# una lista de fechas en las que asistió a clases. Implementa un programa
# en Python que utilice un diccionario para almacenar la información de las
# asistencias. El programa debe permitir registrar la asistencia de los
# estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
# estudiantes y las fechas en las que asistieron.

# (Pista: puedes comenzar con un diccionario vacío y construir un diccionario de listas) 

asistencias = {}

# Función para registrar la asistencia de un estudiante
def registrar_asistencia(nombre_estudiante, fecha):
    if nombre_estudiante not in asistencias:
        asistencias[nombre_estudiante] = []
    asistencias[nombre_estudiante].append(fecha)

# Función para mostrar la lista de estudiantes y sus fechas de asistencia
def mostrar_asistencias():
    for estudiante, fechas in asistencias.items():
        print(f"Estudiante: {estudiante}")
        print("Fechas de asistencia:")
        for fecha in fechas:
            print(f" - {fecha}")

# Bucle para interactuar con el usuario, en el que llama a las funciones anteriores
while True:
    print("\nOpciones:")
    print("1. Registrar asistencia")
    print("2. Mostrar asistencias")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        fecha = input("Fecha de asistencia (DD-MM-YYYY): ")
        registrar_asistencia(nombre, fecha)
    elif opcion == "2":
        mostrar_asistencias()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")