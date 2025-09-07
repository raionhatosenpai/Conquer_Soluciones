# 1º Crea un set y elimina uno de sus elementos.
mi_set = {1, 2, 3, 4, 5}
print(mi_set)
mi_set.remove(3) # Elimina el elemento 3 del set, tambien es valido con .discard() para evitar errores
print(mi_set)
print("-----------------")

# 2º Crea un set vacío.
mi_set_vacio = set()
print(mi_set_vacio)
print("-----------------")

# 3º Crea dos sets y encuentra su union, su intersección y su diferencia

mi_set_1 = {1, 2, 3}
mi_set_2 = {3, 4, 5}
print(mi_set_1)
print(mi_set_2)
print(mi_set_1.union(mi_set_2))
print(mi_set_1.intersection(mi_set_2))
print(mi_set_1.difference(mi_set_2))
print(mi_set_1.symmetric_difference(mi_set_2))  # Diferencia simétrica
print("-----------------")  

# 4º Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.

mi_set_4_a = {1, 2, 3, 4}
mi_set_4_b = {3, 4, 5, 6}
mi_set_4_c = mi_set_4_a.intersection(mi_set_4_b)
print(mi_set_4_a)
print(mi_set_4_b)
print(mi_set_4_c)
print("-----------------")

# 5º .Crea un script que dado un set con números devuelva el numero máximo y mínimo.

mi_set_5 = {1, 2, 3, 4, 5}
print(mi_set_5)
print(max(mi_set_5))
print(min(mi_set_5))
print("-----------------")

# 6º Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets

mi_set_6_a = {1, 2, 3, 4}
mi_set_6_b = {3, 4, 5, 6}
mi_set_6_c = mi_set_6_a.symmetric_difference(mi_set_6_b)
print(mi_set_6_a)
print(mi_set_6_b)
print(mi_set_6_c)
print("-----------------")

# 7º Crea un set con colores y comprueba si cierto color se encuentra en el set

mi_set_7 = {"rojo", "verde", "azul"}
print(mi_set_7)
print("busca el color Rojo: ", "rojo" in mi_set_7)
print("busca el color Amarillo: ", "amarillo" in mi_set_7)
print("-----------------")

# 8º Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo.

mi_set_8_a = {1, 2, 3, 4, "azul"}
mi_set_8_b = {3, 4, 5, 6, "verde"}
mi_set_8_c = mi_set_8_a.difference(mi_set_8_b)
print(mi_set_8_a)
print(mi_set_8_b)
print(mi_set_8_c)
print("-----------------")

# 9º Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.

mi_set_9 = {1, 2, 3, 4, 5}
producto = 1
print(mi_set_9)
for num in mi_set_9:
    producto *= num
print(producto)
