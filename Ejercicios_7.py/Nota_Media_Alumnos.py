# Diccionario o lista de listas y permito añadir nuevos alumnos y sus notas
alumnos = {}
notas = []

# Función para añadir un nuevo alumno y sus notas
def añadir_alumno(alumno, notas):
    if alumno not in alumnos:
        alumnos[alumno] = list(notas)
    else:
        print(f"El alumno {alumno} ya existe. Actualizando sus notas.")
        alumnos[alumno] = list(notas)

# Función para calcular la nota media de un alumno
def calcular_nota_media(alumno):
    if alumno in alumnos:
        notas = alumnos[alumno]
        return sum(notas) / len(notas)
    else:
        return None
    
# Función para mostrar las notas y la nota media de todos los alumnos
def mostrar_notas_y_media():
    for alumno, notas in alumnos.items():
        media = calcular_nota_media(alumno)
        if media is not None:
            print(f"Notas de {alumno}: {notas[-3:]}, Nota media: {media:.2f}")

# Función para la nota media de toda la clase
def media_clase():
    todas_las_notas = [nota for notas in alumnos.values() for nota in notas]
    if todas_las_notas:
        return sum(todas_las_notas) / len(todas_las_notas)
    return 0

# Función para añadir un nuevo alumno
def añadir_nuevo_alumno():
    nombre = input("Introduce el nombre del alumno: ").title()
    notas = input("Introduce las notas del alumno (separadas por comas): ")
    lista_notas = [int(nota.strip()) for nota in notas.split(",") if nota.strip().isdigit()]
    añadir_alumno(nombre, lista_notas)
    if not lista_notas:
     print(f"No se registraron notas válidas para {nombre}. Intenta de nuevo.")
    return

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Añadir nuevo alumno")
    print("2. Mostrar notas y nota media de todos los alumnos")
    print("3. Mostrar nota media de toda la clase")
    print("4. Salir")   

# Bucle principal del programa 
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        añadir_nuevo_alumno()
    elif opcion == "2":
        mostrar_notas_y_media()
    elif opcion == "3":
        print(f"La nota media de toda la clase es: {media_clase():.2f}")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
        continue
# Ejercicio que permite añadir alumnos y sus notas, calcular la nota media de cada alumno y mostrar las notas y medias de todos los alumnos.
# Utiliza un diccionario para almacenar los alumnos y sus notas, y permite añadir nuevos alumnos y sus notas. 
# El programa muestra un menú con opciones para añadir alumnos, mostrar notas y medias, y salir del programa. 
# El bucle principal permite al usuario interactuar con el programa hasta que decida salir. 
