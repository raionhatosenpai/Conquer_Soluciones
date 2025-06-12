# modulo (re) para expresiones regulares 
import re 

# guardo la contraseña en una variable
contraseña = input("Introduce una contraseña: ")

# comprobar si hay una vocal y dos caracteres especiales
if re.search(r"[aeiou]", contraseña) and "*" in contraseña and "#" in contraseña:
    print("Contraseña segura")
else:
    print("Contraseña insegura. Debe contener al menos una vocal (a, e, i, o, u) y dos caracteres especiales (*, #).")