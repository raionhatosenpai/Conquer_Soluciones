# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
# de tus productos. Cada producto tiene un nombre y una cantidad
# vendida. Implementa un programa en Python que utilice un diccionario
# para almacenar la información de las ventas. El programa debe permitir
# registrar las ventas de productos, actualizar la cantidad vendida de un
# producto existente y calcular el total de ventas diarias.
# (Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada producto)

ventas = {}

# Función para registrar una venta
def registrar_venta(nombre_producto, cantidad):
    if nombre_producto in ventas:
        ventas[nombre_producto] += cantidad
    else:
        ventas[nombre_producto] = cantidad

# Función para actualizar una venta existente
def actualizar_venta(nombre_producto, cantidad):
    if nombre_producto in ventas:
        ventas[nombre_producto] = cantidad
    else:
        print("El producto no existe en el registro.")

# Función para calcular el total de ventas
def calcular_total_ventas():
    return sum(ventas.values())

# añadir nuevas ventas usando input()
while True:
    nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre_producto.lower() == "salir":
        break

    if nombre_producto in ventas:
        respuesta = input("Ya existe. ¿Deseas actualizarlo? (s/n): ")
        if respuesta.lower() == "s":
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                actualizar_venta(nombre_producto, nueva_cantidad)
            except ValueError:
                print("Por favor, introduce un número válido.")
            continue  # saltamos al siguiente ciclo
        
    try:
        cantidad = int(input("Ingrese la cantidad vendida: "))
        registrar_venta(nombre_producto, cantidad)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

# Mostrar las ventas registradas
print("Ventas registradas:")
for producto, cantidad in ventas.items():
    print(f"{producto}: {cantidad}")

print(f"Total de ventas: {calcular_total_ventas()}")