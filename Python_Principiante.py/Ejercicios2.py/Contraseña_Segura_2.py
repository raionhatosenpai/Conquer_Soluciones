# modulo (re) para expresiones regulares 
import re 

# guardo la contraseña en una variable
contraseña = input("Introduce una contraseña: ")

# comprobar si hay al menos 8 caracteres, al menos una mayúscula, al menos una minúscula, al menos un número y al menos un carácter especial
if (len(contraseña) >= 8 and
    re.search(r"[A-Z]", contraseña) and
    re.search(r"[a-z]", contraseña) and
    re.search(r"[0-9]", contraseña) and
    re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)):
    
    print("Contraseña segura")
else: # Si no cumple con los requisitos, mostrar un mensaje de error
    print("Contraseña insegura. Debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial.")