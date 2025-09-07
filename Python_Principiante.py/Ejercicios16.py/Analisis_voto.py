# Supongamos que tienes los resultados de una elección con los nombres
# de los candidatos y la cantidad de votos obtenidos por cada uno.
# Implementa un programa en Python que permita registrar los votos,
# mostrar la lista completa de candidatos y sus votos, encontrar al
# candidato ganador (con más votos) y calcular el porcentaje de votos que
# obtuvo cada candidato.

votos = {}

# Función para registrar un voto
def registrar_voto(candidato):
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

# Función para mostrar la lista de candidatos y sus votos
def mostrar_resultados():
    print("\nResultados de la elección:")
    for candidato, cantidad in votos.items():
        print(f"{candidato}: {cantidad} votos")

# Función para encontrar al candidato ganador
def encontrar_ganador():
    if votos:
        ganador = max(votos, key=votos.get)
        print(f"\nEl candidato ganador es: {ganador} con {votos[ganador]} votos")
    else:
        print("No hay votos registrados.")

# Función para calcular el porcentaje de votos por candidato
def calcular_porcentaje_votos():
    total_votos = sum(votos.values())
    if total_votos > 0:
        print("\nPorcentaje de votos por candidato:")
        for candidato, cantidad in votos.items():
            porcentaje = (cantidad / total_votos) * 100
            print(f"{candidato}: {porcentaje:.2f}%")
    else:
        print("No hay votos registrados.")

# Bucle principal del programa
while True:
    print("\nOpciones:")
    print("1. Registrar voto")
    print("2. Mostrar resultados")
    print("3. Encontrar ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        candidato = input("Nombre del candidato: ")
        registrar_voto(candidato)
    elif opcion == "2":
        mostrar_resultados()
    elif opcion == "3":
        encontrar_ganador()
    elif opcion == "4":
        calcular_porcentaje_votos()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
