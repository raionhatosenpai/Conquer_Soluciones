# 22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada
# representa un producto y tiene a su vez las claves "nombre" y "precio" con sus
# respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada
# producto.

productos = {
    "producto1": {"nombre": "Laptop", "precio": 1000},
    "producto2": {"nombre": "Teléfono", "precio": 500},
}

for producto in productos.values():
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']} €")

print("-----------------------")
print("\n")

# 23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor. Imprime el diccionario actualizado.

productos["producto3"] = {"nombre": "Tablet", "precio": 300}

for producto in productos.values():
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']} €")

print("-----------------------")
print("\n")

# 24. Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada
# representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
# respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de
# los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de
# jugadores.

equipos = {
    "equipo1": {"nombre": "Los Tigres", "jugadores": ["Juan", "Pedro", "Luis"]},
    "equipo2": {"nombre": "Las Águilas", "jugadores": ["María", "Ana", "Laura"]},
    "equipo3": {"nombre": "Los Leones", "jugadores": ["Carlos", "Jorge", "Andrés"]}
}

for equipo in equipos.values():
    print(f"Nombre del equipo: {equipo['nombre']}, Jugadores: {', '.join(equipo['jugadores'])}")

print("-----------------------")
print("\n")

# 25. Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
# La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario
# actualizado.

equipos["equipo4"] = {"nombre": "Los Delfines", "jugadores": ["Sofía", "Diego", "Valentina"]}

for equipo in equipos.values():
    print(f"Nombre del equipo: {equipo['nombre']}, Jugadores: {', '.join(equipo['jugadores'])}")

print("-----------------------")
print("\n")

# 26. Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.

equipos["equipo1"]["jugadores"].append("Fernando")

for equipo in equipos.values():
    print(f"Nombre del equipo: {equipo['nombre']}, Jugadores: {', '.join(equipo['jugadores'])}")

print("-----------------------")
print("\n")