import numpy as np

# Crea un arrays lleno de 1s con una longitud dada por el usuario
longitud = int(input("Introduce la longitud del array: "))
array_unos = np.ones(longitud, dtype=int)
print("\nArray de unos:", array_unos)

# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
if filas * columnas == longitud:
    nuevo_array = np.reshape(array_unos, (filas, columnas))
    print("\nArray de unos reestructurado (filas, columnas):", nuevo_array)
else:
    print("Dimensiones incompatibles. filas * columnas debe ser", longitud)