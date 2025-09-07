# Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y, en ese caso:
# 1º Imprima la fila cuyos elementos suman el máximo.
# 2º Imprima la columna cuyos elementos suman el máximo.
# Si no es una matriz (es decir, si las sublistas no tienen la misma longitud), debe devolver dos listas vacías.

import random
# Generación de una matriz aleatoria
fila = random.randint(1, 5)  # <-- Número de filas aleatorias entre 1 y 5
M = []
for _ in range(fila):
    columnas_random = random.randint(1, 5)  # <-- Cada fila tendrá su propio tamaño
    fila_actual = [random.randint(1, 100) for _ in range(columnas_random)]
    M.append(fila_actual)

print("Matriz generada:")
for fila in M:
    print(fila)
suma = sum(num for fila in M for num in fila)
# Imprimir la suma total de los elementos de la matriz
print(f"\nSuma total de los elementos de la matriz: {suma}")
# Funciones para verificar si es una matriz y encontrar la fila y columna con la suma máxima
def es_matriz(M):
    if not M or not isinstance(M, list) or not all(isinstance(fila, list) for fila in M):
        return False
    longitud_fila = len(M[0])
    return all(len(fila) == longitud_fila for fila in M)
# Función para encontrar la fila con la suma máxima
def fila_maxima(M):
    if not es_matriz(M):
        return []
    max_suma = float('-inf')
    fila_max = []
    for fila in M:
        suma_fila = sum(fila)
        if suma_fila > max_suma:
            max_suma = suma_fila
            fila_max = fila
    return fila_max
# Función para encontrar la columna con la suma máxima
def columna_maxima(M):
    if not es_matriz(M):
        return []
    max_suma = float('-inf')
    columna_max = []
    num_columnas = len(M[0])
    for j in range(num_columnas):
        suma_columna = sum(M[i][j] for i in range(len(M)))
        if suma_columna > max_suma:
            max_suma = suma_columna
            columna_max = [M[i][j] for i in range(len(M))]
    return columna_max
# Verificación y ejecución del script
if __name__ == "__main__":
    if es_matriz(M):
        print(f"\nFila con la suma máxima: {fila_maxima(M)}")
        print(f"Columna con la suma máxima: {columna_maxima(M)}")
    else:
        print("\nNo es una matriz válida.")
        print("Fila:", [])
        print("Columna:", [])