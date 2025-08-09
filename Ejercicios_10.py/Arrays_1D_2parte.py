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

# Crea otro array con 15 números decimales aleatorios entre 0 y 1
array_decimales = np.random.rand(15)
print("\nArray de números decimales aleatorios:", array_decimales)

# Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy
suma_elementos = array_aleatorios + array_decimales
print("\nSuma de elementos (operador):", suma_elementos)

suma_elementos = np.add(array_aleatorios, array_decimales)
print("\nSuma de elementos (numpy):", suma_elementos)

# Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
resta_elementos = array_aleatorios - array_decimales
print("\nResta de elementos (operador):", resta_elementos)

resta_elementos = np.subtract(array_aleatorios, array_decimales)
print("\nResta de elementos (numpy):", resta_elementos)

# Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
multiplicacion_elementos = array_aleatorios * array_decimales
print("\nMultiplicación de elementos (operador):", multiplicacion_elementos)

multiplicacion_elementos = np.multiply(array_aleatorios, array_decimales)
print("\nMultiplicación de elementos (numpy):", multiplicacion_elementos)

# Encuentra el valor más alto del primer array que has creado.
maximo_array = np.max(array_aleatorios)
print("\nValor más alto del array de números aleatorios:", maximo_array)