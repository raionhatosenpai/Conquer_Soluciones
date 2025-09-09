#crear un script validador.py
# que contenga una funcion validar_contrasena que reciba una cadena y
# verifique si cumple con los requisitos mínimos de una contraseña segura
# (por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
# minúsculas, números y caracteres especiales).

import string

def validar_contrasena(contrasena):
    return (
        len(contrasena) >= 16 and
        any(c.islower() for c in contrasena) and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena) and
        any(c in string.punctuation for c in contrasena)
    )