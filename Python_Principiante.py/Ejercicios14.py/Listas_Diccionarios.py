# 18. Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario
# representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos
# valores. Recorre la lista e imprime el nombre y edad de cada estudiante.

estudiantes = [
    {"nombre": "Raionhato", "edad": 34},
    {"nombre": "Juan", "edad": 28},
]

for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

print("-----------------------")
print("\n")

# 19. Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las mismas claves "nombre" y "edad". Imprime la lista actualizada.

nuevo_estudiante = {"nombre": "Maria", "edad": 22}
estudiantes.append(nuevo_estudiante)

for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

print("-----------------------")
print("\n")

# 20. Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
del estudiantes[1]

for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

print("-----------------------")
print("\n")

# 21. Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. Imprime la lista actualizada.

estudiantes[0]["edad"] = 201

for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

print("-----------------------")
print("\n")