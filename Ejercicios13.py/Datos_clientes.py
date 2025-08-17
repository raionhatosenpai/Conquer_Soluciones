# Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
# el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
# segunda base de datos contiene el nombre del cliente, la dirección y el historial de
# pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
# devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
# ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre.

# Pista: Tus datos de entrada podrían ser así —>
# base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")]
# base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

import numpy as np

# Bases de  datos
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012"), ("Luis", "luis@example.com", "555-3456"), ("Nacho", "nacho@example.com", "555-7890")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"]), ("Pedro", "Calle 101", ["Libro5"]), ("Ana", "Calle 102", ["Libro6"])]

# Crear un set de nombres de la primera base de datos
nombres_base1 = {cliente[0] for cliente in base_datos1}
nombres_base2 = {cliente[0] for cliente in base_datos2}
print(sorted(nombres_base1.intersection(nombres_base2)))  # Imprime solo los nombres comunes ordenados
print("-----------------------------------------")

# Otro modo de hacerlo seria:
clientes_comunes = [cliente for cliente in base_datos2 if cliente[0] in nombres_base1]
print(sorted(clientes_comunes))