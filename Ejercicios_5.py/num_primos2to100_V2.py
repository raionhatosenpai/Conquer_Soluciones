# Ejercicio: Imprimir los números primos del 2 al 100 version 2
# Esta versión utiliza un enfoque diferente para determinar si un número es primo.
# un metodo alternativo para determinar si un número es primo, mucho más eficiente
for i in range(2, 101):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end='  ')