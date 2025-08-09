import numpy as np

# Crea un array con 15 números enteros aleatorios entre 1 y 100
array_aleatorios = np.random.randint(1, 101, size=15)
print("\nArray de números aleatorios:", array_aleatorios)

# Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados
producto = 1
for num in array_aleatorios:
    producto *= int(num) # Aseguramos que sea un entero
print("\nProducto de elementos del array (bucle):", producto)

producto_np = np.prod(array_aleatorios, dtype=object) # Aseguramos que sea un objeto
print("\nProducto de elementos del array (numpy):", producto_np)
print("-------------------------------------------------------------------")

# Crea otro array con 15 números decimales aleatorios entre 0 y 1
array_decimales = np.random.rand(15)
print("\nArray de números decimales aleatorios:", array_decimales)
print("-------------------------------------------------------------------")

# Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy
suma_elementos = array_aleatorios + array_decimales
print("\nSuma de elementos (operador):", suma_elementos)


suma_elementos = np.add(array_aleatorios, array_decimales)
print("\nSuma de elementos (numpy):", suma_elementos)
print("-------------------------------------------------------------------")

# Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
resta_elementos = array_aleatorios - array_decimales
print("\nResta de elementos (operador):", resta_elementos)


resta_elementos = np.subtract(array_aleatorios, array_decimales)
print("\nResta de elementos (numpy):", resta_elementos)
print("-------------------------------------------------------------------")

# Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
multiplicacion_elementos = array_aleatorios * array_decimales
print("\nMultiplicación de elementos (operador):", multiplicacion_elementos)
print("-------------------------------------------------------------------")

multiplicacion_elementos = np.multiply(array_aleatorios, array_decimales)
print("\nMultiplicación de elementos (numpy):", multiplicacion_elementos)
print("-------------------------------------------------------------------")

# Encuentra el valor más alto del primer array que has creado.
maximo_array = np.max(array_aleatorios)
print("\nValor más alto del array de números aleatorios:", maximo_array)
print("-------------------------------------------------------------------")

# Calcula la media (mean), la mediana (median) y al deviación estandar (standard deviation) de los arrays
array_aleatorios_mean = np.mean(array_aleatorios)
array_aleatorios_median = np.median(array_aleatorios)
array_aleatorios_std = np.std(array_aleatorios)
print("\nMedia del array de números aleatorios:", array_aleatorios_mean)
print("\nMediana del array de números aleatorios:", array_aleatorios_median)
print("\nDesviación estándar del array de números aleatorios:", array_aleatorios_std)
print("-------------------------------------------------------------------")

# # Calcula la media (mean), la mediana (median) y al deviación estandar (standard deviation) de los arrays (decimales)
array_decimales_mean = np.mean(array_decimales)
array_decimales_median = np.median(array_decimales)
array_decimales_std = np.std(array_decimales)
print("\nMedia del array de números decimales aleatorios:", array_decimales_mean)
print("\nMediana del array de números decimales aleatorios:", array_decimales_median)
print("\nDesviación estándar del array de números decimales aleatorios:", array_decimales_std)
print("-------------------------------------------------------------------")