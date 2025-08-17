# Crea un programa que tome una base de datos de una red social como una lista de
# tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
# nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
# diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
# tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

# Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro", 
# "Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Pista 2: Para eliminar duplicidades puedes usar sets

import numpy as np
# Crear una lista de tuplas
red_social = [("Juan", ["Maria", "Pedro", "Luis", "Ana"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria", "Juan", "Luis", "Maria"]), ("Luis", ["Juan", "Ana", "Maria", "Nacho"]),
              ("Ana", ["Juan", "Pedro", "Luis", "Nacho"]), ("Nacho", ["Juan", "Maria", "Ana", "Pedro", "Luis", "Juan", "Juan"])]

# Eliminar duplicados
red_social_limpia = [(usuario, list(set(amigos))) for usuario, amigos in red_social]

# Contar amigos
contador_amigos = [(usuario, len(amigos)) for usuario, amigos in red_social_limpia]

# Encontrar usuario con más amigos
usuario_mas_amigos = max(contador_amigos, key=lambda x: x[1]) 
# key=lambda x: x[1] indica que la comparación se hace usando el segundo elemento de cada tupla.

# Devolver resultado
resultado = (tuple(contador_amigos), "El usuario con más amigos es: " + usuario_mas_amigos[0])
print(resultado)
