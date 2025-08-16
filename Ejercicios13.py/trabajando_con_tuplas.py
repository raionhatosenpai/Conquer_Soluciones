# OBJETIVO: FAMILIARIZACIÓN CON EL USO DE TUPLAS Y SETS,
# SUS CARACTERÍSTICAS Y METODOS ASOCIADOS

# 1º Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea

mi_tupla = ("hola", 777, True)

print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[2]) 
print("-----------------")
# se puede crear un bucle: 
for elemento in mi_tupla:
    print(elemento)

# 2º Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias?

mi_lista = ["hola", 777, True]
mi_lista[0] = "adios"
mi_lista[1] = 888
mi_lista[2] = False
print(mi_lista)
print("-----------------")

# Intentando modificar la tupla
# mi_tupla_2 = ("hola", 777, True)
# mi_tupla_2[0] = "adios"
# mi_tupla_2[1] = 888
# mi_tupla_2[2] = False
# print(mi_tupla_2) # Esto dará un error porque las tuplas son inmutables
# print("-----------------")

# 3º Crea una tupla de enteros y devuelve la suma de los elementos

mi_tupla_3 = (1, 2, 3, 4, 5)
suma = sum(mi_tupla_3)
print(mi_tupla_3)
print(suma)
print("-----------------")

# 4º Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.

mi_tupla_4 = ("hola", "adios", "buenos dias")
nueva_tupla = tuple(s[0] for s in mi_tupla_4)
print(mi_tupla_4)
print(nueva_tupla)
print("-----------------")

# 5º Crea un script que dada una tupla de números devuelva el producto de todos los números pares.

mi_tupla_5 = (1, 2, 3, 4, 5, 6)
producto = 1
for n in mi_tupla_5:
    if n % 2 == 0:
        producto *= n
print(mi_tupla_5)
print(producto)
print("-----------------")

# 6º Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente

mi_tupla_6 = (5, 2, 9, 1, 3, 4, 6, 7, 8)
nueva_tupla_6 = tuple(sorted(mi_tupla_6, reverse=True))
print(mi_tupla_6)
print(nueva_tupla_6)
print("-----------------")

# 7º Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).

mi_tupla_7 = (1, 2, 2, 3, 4, 4, 5)
nueva_tupla_7 = tuple(set(mi_tupla_7))
print(mi_tupla_7)
print(nueva_tupla_7)
print("-----------------")

# 8º Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.

mi_tupla_8 = (1, 2, 3, 4, 5)
numero_a_buscar = int(input("Introduce un número a buscar en la tupla: "))
resultado = numero_a_buscar in mi_tupla_8
print(mi_tupla_8)
print(resultado)
print("-----------------")

# 9º Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.

mi_tupla_9_a = (1, 2, 3)
mi_tupla_9_b = ("a", "b", "c")
nueva_tupla_9 = mi_tupla_9_a + mi_tupla_9_b
print(mi_tupla_9_a)
print(mi_tupla_9_b)
print(nueva_tupla_9)
print("-----------------")

# 10º Crea un script que dada una tupla de números devuelva el máximo y el mínimo

mi_tupla_10 = (5, 2, 9, 1, 3, 4, 6, 7, 8)
maximo = max(mi_tupla_10)
minimo = min(mi_tupla_10)
print(mi_tupla_10)
print(maximo)
print(minimo)
print("-----------------")

# 11º Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).

mi_tupla_11 = ("hola", "adios", "buenos dias")
mas_largo = max(mi_tupla_11, key=len)
mas_corto = min(mi_tupla_11, key=len)
print(mi_tupla_11)
print(mas_largo)
print(mas_corto)
print("-----------------")

# 12º Crea un script que dada una tupla devuelva el contenido en orden revertido

mi_tupla_12 = (1, 2, 3, 4, 5)
nueva_tupla_12 = tuple(reversed(mi_tupla_12)) # nueva_tupla_12 = mi_tupla_12[::-1] es valido
print(mi_tupla_12)
print(nueva_tupla_12)
print("-----------------")

# 13º  Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
# elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
# elementos de la tupla interna correspondiente.

mi_tupla_13 = ((1, 2), (3, 4), (5, 6))
nueva_tupla_13 = tuple(a + b for a, b in mi_tupla_13)
print(mi_tupla_13)
print(nueva_tupla_13)
print("-----------------")
