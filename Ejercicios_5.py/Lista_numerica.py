# crear una lista de números y realizar varias operaciones
numeros = [1,2,3,4,5,6,7,8,9,10]
print("Lista de números:", numeros)

# tomar solo los numeros pares de la lista e imprimirlos en orden inverso
numeros_pares_invertidos = [num for num in numeros[::-1] if num % 2 == 0]
print("Números pares:", numeros_pares_invertidos)

# crear bulce para impimir el cuadrado de cada número
for num in numeros:
    print(f"El cuadrado de {num} es:", num ** 2)

# hallar el numero mas pequeño de la lista
numero_mas_pequeno = min(numeros)
print("Número más pequeño:", numero_mas_pequeno)

# hallar el numero mas grande de la lista
numero_mas_grande = max(numeros)
print("Número más grande:", numero_mas_grande)

# sumar todos los números de la lista con un bucle
suma_con_bucle = 0
for num in numeros:
    suma_con_bucle += num
print("Suma con bucle:", suma_con_bucle)
# Sumar todos los números de la lista sin usar un bucle
suma_sin_bucle = sum(numeros)
print("Suma sin bucle:", suma_sin_bucle)

# encontrar el indice de un número específico (por ejemplo, 8)
indice_numero = numeros.index(8) if 8 in numeros else -1
print("Índice del número 8:", indice_numero)

# hacer el paso anterior pero con la lista del punto n° 2
indice_numero_pares = numeros_pares_invertidos.index(8) if 8 in numeros_pares_invertidos else -1
print("Índice del número 8 en números pares:", indice_numero_pares)