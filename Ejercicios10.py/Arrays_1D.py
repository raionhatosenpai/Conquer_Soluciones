import numpy as np
# Array de ceros (8 elementos), Crea un array de longitud fija y dtype por defecto.
array_ceros = np.zeros(8)
print("Array de ceros:", array_ceros)

# Poner todos los elementos a 2
array_ceros[:] = 2 # tambien es valido array_ceros.fill(2)
print("\nArray de ceros modificado:", array_ceros)

# Array con pares del 1 al 10
array_pares = np.arange(2, 11, 2)
print("\nArray de pares del 1 al 10:", array_pares)

# Suma de elementos del array, suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados
suma_pares = 0
for num in array_pares:
    suma_pares += num
print("\nSuma de elementos del array de pares (bucle):", suma_pares)

suma_pares = np.sum(array_pares)
print("\nSuma de elementos del array de pares (numpy):", suma_pares)

# Revierte array_2 y guárdalo en una variable independiente.
array_pares_invertido = np.flip(array_pares)
print("\nArray de pares revertido:", array_pares_invertido)

# Elementos comunes
elementos_comunes = np.intersect1d(array_ceros, array_pares_invertido)
print("\nElementos comunes entre array de ceros y array de pares:", elementos_comunes)

# Crea un arrays lleno de 1s con una longitud dada por el usuario
longitud = int(input("\nIntroduce la longitud del array de unos: "))
array_unos = np.ones(longitud)
print("Array de unos:", array_unos)