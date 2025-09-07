# Crea un programa que tome la lista
# de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
# libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
# libro y el apellido del autor.

# Pista: Tus datos de entrada podrían ser así —> lista_libros = [(‘El aleph', ‘Jorge Luis
# Borges'), ('Cien años de soledad', ‘Gabriel Garcia Márquez'), ('La ciudad y los perros',
# ‘Mario Vargas Llosa')] 

import numpy as np

# Crear una lista de tuplas con libros y autores
lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Gabriel Garcia Márquez'), ('Nuestra señora de París', 'Victor Hugo'), 
                ('Crimen y castigo', 'Fiódor Dostoyevski'), ('El conde de montecristo', 'Alexandre Dumas'), ('Cartas del diablo a su sobrino', 'C.S. Lewis')]

# Crear una nueva lista de tuplas con el título del libro y el apellido del autor
nueva_lista = [(titulo, autor.split()[-1]) for titulo, autor in lista_libros]
print(nueva_lista)
