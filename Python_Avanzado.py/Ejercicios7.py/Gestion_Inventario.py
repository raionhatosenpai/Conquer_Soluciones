'''magina que trabajas en una empresa de logística y tu tarea es desarrollar un 
sistema de gestión de inventario. El inventario está representado como una lista 
de productos ordenados por sus códigos. Cada producto se describe como un 
diccionario con las claves 'codigo' y 'cantidad'.
Tu objetivo es implementar una función recursiva que realice una búsqueda 
binaria en este inventario y devuelva la cantidad disponible para un producto 
específico, dado su código'''

def busqueda_binaria(inventario, codigo, inicio, fin):
    if inicio > fin:
        return 0  # Código no encontrado, cantidad es 0

    medio = (inicio + fin) // 2
    producto = inventario[medio]

    if producto['codigo'] == codigo:
        return producto['cantidad']
    elif producto['codigo'] < codigo:
        return busqueda_binaria(inventario, codigo, medio + 1, fin)
    else:
        return busqueda_binaria(inventario, codigo, inicio, medio - 1)
# Ejemplo de uso
inventario = [
    {'codigo': 'A001', 'cantidad': 50},
    {'codigo': 'A002', 'cantidad': 20},
    {'codigo': 'A003', 'cantidad': 0},
    {'codigo': 'A004', 'cantidad': 15},
    {'codigo': 'A005', 'cantidad': 30}
    ]

while True:
    codigo_buscar = input("Ingrese el código del producto a buscar (o 'salir' para terminar): ")
    if codigo_buscar.lower() == 'salir':
        break
    cantidad = busqueda_binaria(inventario, codigo_buscar, 0, len(inventario) - 1)
    if cantidad > 0:
        print(f"Cantidad disponible para el producto {codigo_buscar}: {cantidad}")
    else:
        print(f"Producto {codigo_buscar} no encontrado o sin stock.")