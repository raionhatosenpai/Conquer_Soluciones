import numpy as np

# Crea un arrays lleno de 1s con una longitud dada por el usuario
longitud = int(input("Introduce la longitud del array: "))
array_unos = np.ones(longitud, dtype=int)
print("\nArray de unos:", array_unos)

# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
n = array_unos
filas = int(input("Filas: "))
n = n.reshape(filas, -1)   # NumPy calcula columnas si es divisible
if filas * n.shape[1] != n.size:
    print("Dimensiones incompatibles. filas * columnas debe ser", n.size)
else:
    n = n.reshape(filas, -1)
print("\nArray de unos reestructurado (filas, columnas):", n)