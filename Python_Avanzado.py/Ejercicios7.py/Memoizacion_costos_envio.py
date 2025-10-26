'''Imagina que estás trabajando en un sistema de gestión de costos de envío para una empresa de logística.
El sistema debe calcular el costo de envío para diferentes destinos, distancias y pesos de paquetes.
Implementa una función llamada calcular_costo_envio que tome como entrada un destino, una distancia 
en kilómetros y un peso en kilogramos, y devuelva el costo total del envío.

Requerimientos:
1. El costo base de envío es de $5.0.
2. El costo por kilómetro de distancia es de $0.1.
3. El costo por kilogramo de peso es de $0.2.

Implementa la función de manera eficiente utilizando memoización para evitar 
recalcular el costo para los mismos destinos, distancias y pesos'''

def calcular_costo_envio(destino, distancia_km, peso_kg, memo={}):
    # Crear una clave única para la combinación de destino, distancia y peso
    clave = (destino, distancia_km, peso_kg)

    # Verificar si el costo ya ha sido calculado
    if clave in memo:
        print("✅ Costo obtenido desde la caché.")
        return memo[clave]
    else:
        print("🧮 Calculando nuevo costo...")

    # Costos base y por unidad
    costo_base = 5.0
    costo_por_km = 0.1
    costo_por_kg = 0.2

    # Calcular el costo total
    costo_total = costo_base + (costo_por_km * distancia_km) + (costo_por_kg * peso_kg)

    # Almacenar el resultado en el diccionario de memoización
    memo[clave] = costo_total

    return costo_total

# Ejemplo de uso
while True:
    destino = input("Ingrese el destino del envío (o 'salir' para terminar): ")
    if destino.lower() == 'salir':
        break
    distancia = float(input("Ingrese la distancia en kilómetros: "))
    peso = float(input("Ingrese el peso en kilogramos: "))

    costo = calcular_costo_envio(destino, distancia, peso)
    print(f"El costo total de envío a {destino} es: ${costo:.2f}\n")