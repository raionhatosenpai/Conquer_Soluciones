# crear otro script creador.py con una función llamada
# generar_contrasena que genere contraseñas seguras de forma aleatoria. 
# La función debe permitir especificar la longitud de la contraseña y qué tipos de
# caracteres deben incluirse (por ejemplo, letras mayúsculas, letras minúsculas, números y caracteres especiales).

import random
import string

def generar_contrasena(longitud=16, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    caracteres = ""
    if incluir_mayusculas: caracteres += string.ascii_uppercase
    if incluir_minusculas: caracteres += string.ascii_lowercase
    if incluir_numeros: caracteres += string.digits
    if incluir_especiales: caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")
    
    return ''.join(random.choice(caracteres) for _ in range(longitud))
