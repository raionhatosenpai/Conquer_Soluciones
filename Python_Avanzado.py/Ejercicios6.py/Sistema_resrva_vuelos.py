#  Crea un sistema de clases que permita a los usuarios realizar reservas de vuelos. 
# Clase base: 'Vuelo'
# - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de pasajeros
# - Métodos: agregar pasajero, verificar disponibilidad de asientos
# - Clase derivada: 'VueloEspecial' (hereda de 'Vuelo')
# - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, trabajo)

class Vuelo:
    # Atributos: número de vuelo, origen, destino, capacidad máxima, lista de pasajeros
    # Métodos: agregar pasajero, verificar disponibilidad de asientos
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_maxima = capacidad_maxima
        self.lista_pasajeros = []

    # Métodos: agregar pasajero, verificar disponibilidad de asientos
    def agregar_pasajero(self, nombre_pasajero):
        if self.verificar_disponibilidad_asientos():
            self.lista_pasajeros.append(nombre_pasajero)
            print(f"Pasajero {nombre_pasajero} agregado al vuelo {self.numero_vuelo}.")
        else:
            print(f"No hay asientos disponibles en el vuelo {self.numero_vuelo}.")
    
    # Verificar disponibilidad de asientos
    def verificar_disponibilidad_asientos(self):
        return len(self.lista_pasajeros) < self.capacidad_maxima

    # Mostrar información del vuelo
    def mostrar_informacion(self):
        print(f"Vuelo {self.numero_vuelo}: {self.origen} → {self.destino}")
        print(f"Capacidad: {self.capacidad_maxima}, Pasajeros actuales: {len(self.lista_pasajeros)}")
        print("Lista de pasajeros:")
        for i in range(self.capacidad_maxima):
            if i < len(self.lista_pasajeros):
                print(f"Asiento {i+1}: {self.lista_pasajeros[i]}")
            else:
                print(f"Asiento {i+1}: Vacío")

# Clase derivada: 'VueloEspecial' (hereda de 'Vuelo')
# Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, trabajo)
class VueloEspecial(Vuelo):
    # Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, trabajo)
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima, motivo_vuelo):
        super().__init__(numero_vuelo, origen, destino, capacidad_maxima)
        self.motivo_vuelo = motivo_vuelo
        
    # Mostrar información del vuelo especial
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Motivo del vuelo especial: {self.motivo_vuelo}")


# ----- EJEMPLO DE USO -----
# Preguntar si el usuario quiere un vuelo normal o especial
tipo = input("¿Desea crear un vuelo normal (n) o especial (e)? ").lower()

if tipo == 'n':
    motivo = None
    numero = input("Número del vuelo: ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    try:
        capacidad = int(input("Capacidad máxima de pasajeros: "))
    except ValueError:
        print("Por favor, introduce un número válido para la capacidad.")
        exit()

    vuelo = Vuelo(numero, origen, destino, capacidad)

elif tipo == 'e':
    numero = input("Número del vuelo: ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    try:
        capacidad = int(input("Capacidad máxima de pasajeros: "))
    except ValueError:
        print("Por favor, introduce un número válido para la capacidad.")
        exit()

    motivo = input("Motivo del vuelo especial (vacaciones, trabajo, etc.): ")
    vuelo = VueloEspecial(numero, origen, destino, capacidad, motivo)

else:
    print("Opción inválida.")
    exit()

# Menú para agregar pasajeros
while True:
    print("\n--- MENÚ ---")
    accion = input("¿Desea agregar un pasajero (a), mostrar información (m) o salir (q)? ").lower()
    if accion == 'a':
        if vuelo.verificar_disponibilidad_asientos():
            nombre_pasajero = input("Ingrese el nombre del pasajero: ").title()
            vuelo.agregar_pasajero(nombre_pasajero)
        else:
            print("El vuelo ya está completo.")
    elif accion == 'm':
        vuelo.mostrar_informacion()
    elif accion == 'q':
        print("Saliendo del programa.")
        break
    else:
        print("Acción no reconocida.")
