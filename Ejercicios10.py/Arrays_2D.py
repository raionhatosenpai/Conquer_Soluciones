import numpy as np

# Crea un arrays lleno de 1s con una longitud dada por el usuario
longitud = int(input("Introduce la longitud del array: "))
array_unos = np.ones(longitud, dtype=int)
print("\nArray de unos:", array_unos)
print("-------------------------------------------------------------------")

# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
if filas * columnas == longitud:
    nuevo_array = np.reshape(array_unos, (filas, columnas))
    print("Array de unos reestructurado (filas, columnas):\n", nuevo_array)
else:
    print("Dimensiones incompatibles. filas * columnas debe ser\n", longitud)
print("-------------------------------------------------------------------")

# Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
if filas == columnas:
    matriz_identidad = np.eye(filas, dtype=int)
    print("\nMatriz identidad (filas, columnas):\n", matriz_identidad)
else:
    print("Dimensiones incompatibles. filas debe ser igual a columnas.")
print("-------------------------------------------------------------------")

# Concatena ambas estructuras horizontalmente y verticalmente (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)
if filas == columnas:
    matriz_identidad = np.eye(filas, dtype=int)
    print("\nMatriz identidad (filas, columnas):\n", matriz_identidad)

    # concatena horizontalmente los dos arrays
    concat_horizontal = np.concatenate((nuevo_array, matriz_identidad), axis=1)
    print("\nConcatenación horizontal:\n", concat_horizontal)

    # concatena verticalmente los dos arrays
    concat_vertical = np.concatenate((nuevo_array, matriz_identidad), axis=0)
    print("\nConcatenación vertical:\n", concat_vertical)
else:
    print("Dimensiones incompatibles. filas debe ser igual a columnas.")
print("-------------------------------------------------------------------")

if filas == columnas:
    matriz_identidad = np.eye(filas, dtype=int)
    print("\nMatriz identidad (filas, columnas):\n", matriz_identidad)

    # concatena horizontalmente los dos arrays (usando hstack)
    concat_horizontal = np.hstack((nuevo_array, matriz_identidad))
    print("\nConcatenación horizontal (hstack):\n", concat_horizontal)

    # concatena verticalmente los dos arrays (usando vstack)
    concat_vertical = np.vstack((nuevo_array, matriz_identidad))
    print("\nConcatenación vertical (vstack):\n", concat_vertical)
else:
    print("Dimensiones incompatibles. filas debe ser igual a columnas.")
print("-------------------------------------------------------------------")
