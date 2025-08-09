#  Encontrar duplicados, mover a otra lista, y dejar solo los únicos
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13]
lista_duplicados = []
lista_unicos = []
# Encontrar duplicados, mover a otra lista, y dejar solo los únicos
for num in lista_original:
    if num not in lista_duplicados:
        if lista_original.count(num) > 1:
            lista_duplicados.append(num)
        else:
            lista_unicos.append(num)
print("Lista original:", lista_original)
print("Lista de duplicados:", lista_duplicados)
print("Lista de únicos:", lista_unicos)
print("\n")

# unir dos listas y ordenarlas
lista_ordenada = lista_unicos + lista_duplicados
lista_ordenada.sort()
print("Lista unida y ordenada:", lista_ordenada)
print("\n")

# Escribe un script que encuentre el segundo número más grande de una lista.
lista_numeros = lista_ordenada  # Usamos la lista ordenada del ejercicio anterior
primer_mayor = segundo_mayor = float('-inf')
for num in lista_numeros:
    if num > primer_mayor:
        segundo_mayor = primer_mayor
        primer_mayor = num
    elif num > segundo_mayor and num != primer_mayor:
        segundo_mayor = num
print("El segundo número más grande es:", segundo_mayor)
print("\n")

# Crea un script que cuente el número de elementos más grandes que un determinado número
# dado por el usuario (supón una lista numérica)
numero_usuario = int(input("Introduce un número: "))
contador = sum(1 for num in lista_numeros if num > numero_usuario)
print("Cantidad de números mayores que", numero_usuario, "es:", contador)
print("\n")

# Crea un script dado un número introducido por el usuario o determinado al inicio del
# programa, realice la suma de aquellos números que sean divisibles por este. 
numero_divisor = int(input("Introduce un número divisor: "))
suma_divisibles = sum(num for num in lista_numeros if num % numero_divisor == 0)
print("La suma de los números divisibles por", numero_divisor, "es:", suma_divisibles)
print("\n")

# Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.
numero_usuario_alto = int(input("Introduce un número para encontrar el más alto inferior: "))
numero_mas_alto_inferior = max((num for num in lista_numeros if num < numero_usuario_alto), default=None)
if numero_mas_alto_inferior is not None:
    print("El número más alto inferior a", numero_usuario_alto, "es:", numero_mas_alto_inferior)
print("\n")

# Crea un script que extraiga los elementos comunes entre dos listas e imprima el resultado sin duplicados.
lista1 = lista_original
lista2 = lista_ordenada
elementos_comunes = list(set(num for num in lista1 if num in lista2))
print("Elementos comunes:", elementos_comunes)
print("\n")

# Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
elemento_buscado = int(input("Introduce un número para contar sus apariciones: "))
contador_apariciones = lista_original.count(elemento_buscado)
print("El número", elemento_buscado, "aparece", contador_apariciones, "veces en la lista.")
print("\n")

# Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.
lista_enteros = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print("Lista original:", lista_enteros)
nueva_lista_positivos = [num for num in lista_enteros if num > 0]
print("Lista de números positivos:", nueva_lista_positivos)
print("\n")

# Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
# los strings de la lista original.
lista_strings = ["hola", "mundo", "python", "es", "genial"]
print("Lista de strings:", lista_strings)
nueva_lista_tamagnos = [len(s) for s in lista_strings]
print("Lista de tamaños de strings:", nueva_lista_tamagnos)
print("\n")

# Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
# mayúscula en una sola línea.
nueva_lista_mayusculas = [s.upper() for s in lista_strings] # Convertir a mayúsculas la lista del ejercicio anterior
print("Strings en mayúscula :", " ".join(nueva_lista_mayusculas))
print("\n")
