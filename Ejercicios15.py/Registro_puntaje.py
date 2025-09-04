 # Implementa un programa en Python que permita registrar y mantener un
# seguimiento de los puntajes de un juego. El programa debe permitir a los
# jugadores ingresar sus nombres y puntajes, almacenarlos en un
# diccionario y proporcionar funcionalidades para mostrar el puntaje más
# alto, el promedio de puntajes y la cantidad total de jugadores.

puntajes = {}

# Función para agregar un puntaje
def agregar_puntaje(nombre_jugador, puntaje):
    puntajes[nombre_jugador] = puntaje

# Función para mostrar el puntaje más alto
def mostrar_puntaje_alto():
    if puntajes:
        jugador_alto = max(puntajes, key=puntajes.get)
        print(f"El puntaje más alto es de {jugador_alto}: {puntajes[jugador_alto]}")
    else:
        print("No hay puntajes registrados.")

# Función para mostrar el promedio de puntajes
def mostrar_promedio_puntajes():
    if puntajes:
        promedio = sum(puntajes.values()) / len(puntajes)
        print(f"El promedio de puntajes es: {promedio}")
    else:
        print("No hay puntajes registrados.")

# Función para mostrar la cantidad total de jugadores
def mostrar_total_jugadores():
    print(f"Total de jugadores: {len(puntajes)}")

# Bucle para interactuar con el usuario
while True:
    print("\nOpciones:")
    print("1. Agregar puntaje")
    print("2. Mostrar puntaje más alto")
    print("3. Mostrar promedio de puntajes")
    print("4. Mostrar total de jugadores")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del jugador: ")
        puntaje = int(input("Puntaje: "))
        agregar_puntaje(nombre, puntaje)
    elif opcion == "2":
        mostrar_puntaje_alto()
    elif opcion == "3":
        mostrar_promedio_puntajes()
    elif opcion == "4":
        mostrar_total_jugadores()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")