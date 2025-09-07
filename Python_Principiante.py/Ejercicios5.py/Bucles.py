num_estrellas = int(input("Introduce un número entero : "))
# Imprimir un triángulo de estrellas ascendente y descendente
# Parte ascendente
print()  # Para añadir una nueva línea antes de empezar el triángulo 
for i in range(num_estrellas):
    i = i + 1
    print("*" * i , end=" ")
    print()  # Para añadir una nueva línea después de cada fila
# Parte descendente
for i in range(num_estrellas - 1, 0, -1):
    print("*" * i, end=" ")
    print()  # Para añadir una nueva línea después de cada fila
print()  # Para añadir una nueva línea al final