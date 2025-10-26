'''Imagina que estás trabajando en un sistema de análisis de datos y te han 
proporcionado una lista de números enteros. Tu tarea es desarrollar una 
función llamada max_subarray_sum que encuentre y devuelva la suma máxima de 
un subarreglo contiguo en la lista.

Por ejemplo, considera la lista [1, -2, 3, 10, -4, 7, 2, -5] . 
El subarreglo contiguo con la suma máxima es [3, 10, -4, 7, 2] , y la suma de esos elementos es 18.
Por lo tanto, la función debería devolver 18 para esta lista.

Implementa la función max_subarray_sum y, además, aplica memoización para 
mejorar su eficiencia en el cálculo de subarreglos de suma máxima en listas 
previamente procesadas'''

def max_subarray_sum(arr, memo=None):
    # Convertir la lista a una tupla para usarla como clave en el diccionario de memoización
    if memo is None:
        memo = {}

    arr_tuple = tuple(arr)
    if arr_tuple in memo:
        return memo[arr_tuple]

    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    memo[arr_tuple] = max_sum
    return max_sum

# Ejemplo de uso
if __name__ == "__main__":
    lista_numeros = [1, -2, 3, 10, -4, 7, 2, -5]
    resultado = max_subarray_sum(lista_numeros)
    print(f"La suma máxima del subarreglo es: {resultado}")  # Debería imprimir 18