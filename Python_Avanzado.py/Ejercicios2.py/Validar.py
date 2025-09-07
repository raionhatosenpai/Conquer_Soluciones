import string

def validar_contrasena(contrasena):
    return (
        len(contrasena) >= 16 and
        any(c.islower() for c in contrasena) and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena) and
        any(c in string.punctuation for c in contrasena)
    )