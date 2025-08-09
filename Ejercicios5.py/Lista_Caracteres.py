# Crear una lista de frutas y realizar varias operaciones
# Imprimir cada fruta en una línea separada
frutas = ["manzana", "banana", "cereza", "pera", "higo", "frambuesa", "fresa"]
print("Lista de frutas:", frutas)
len_frutas = len(frutas)
print("Número de frutas:", len_frutas)

# Imprimir la fruta que se encuentra en la posición 3 (índice 2)
print("la fruta que se encuentra en la posición 3 es:", frutas[2])  # Recordar que la posición 3 es el índice 2

# Cambiar la fruta en la posición 2 (índice 1) a "mora"
frutas[1] = "mora"
print("Lista de frutas después de cambiar la fruta en la posición 2:", frutas)

# Agregar una nueva fruta al final de la lista
fruta_agregada = "mango"
frutas.append(fruta_agregada)
print("Lista de frutas después de agregar una nueva fruta:", frutas)

# añadir una nueva fruta al principio de la lista
frutas.insert(0, "uva")
print("Lista de frutas después de añadir una nueva fruta al principio:", frutas)

# crear un bucle que imprima cada fruta en una línea separada
for fruta in frutas:
    print("Fruta:", fruta)

# utilizar pop para eliminar la última fruta de la lista y guardar el valor eliminado en una variable
removed_fruit = frutas.pop()
print("Lista de frutas después de eliminar la última fruta:", frutas)
print("Fruta eliminada:", removed_fruit)

# otro bucle que imprima cada fruta en una línea separada
print("Frutas restantes en la lista:")
for fruta in frutas:
    print("Fruta:", fruta)

# crear un script que imprima la longitud del nombre de cada fruta
print("Longitud del nombre de cada fruta:")
for fruta in frutas:
    print(f"La longitud de '{fruta}' es:", len(fruta))

# bucle que imprima solo las frutas que tienen más de 5 letras
print("Frutas con más de 5 letras:")
for fruta in frutas:
    if len(fruta) > 5:
        print("Fruta:", fruta)

# usar remove() para eliminar una fruta específica de la lista
fruta_a_eliminar = "cereza"
frutas.remove(fruta_a_eliminar)
print("Lista de frutas después de eliminar la fruta:", frutas)

# usar clear() para vaciar la lista de frutas
frutas.clear()
print("Lista de frutas después de vaciarla:", frutas)