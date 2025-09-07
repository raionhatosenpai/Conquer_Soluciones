# CONTRASENA SEGURA
# Crea un script que solicite una contraseña, analice si es segura y si no lo es
# sugiera una nueva contraseña. Para ello puedes crear un script validador.py
# que contenga una funcion validar_contrasena que reciba una cadena y
# verifique si cumple con los requisitos mínimos de una contraseña segura
# (por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
# minúsculas, números y caracteres especiales). La función debe devolver un
# valor booleano que indique si la contraseña es válida o no. 
# Por otro lado puedes crear otro script creador.py con una función llamada
# generar_contrasena que genere contraseñas seguras de forma aleatoria. 
# La función debe permitir especificar la longitud de la contraseña y qué tipos de
# caracteres deben incluirse (por ejemplo, letras mayúsculas, letras minúsculas, números y caracteres especiales).
# (Para el generador de contraseñas puedes probar a usar los modulos random y string)


from Validar import validar_contrasena
from Creador import generar_contrasena

# Solicitar contraseña al usuario
contrasena = input("Introduce una contraseña: ")

while not validar_contrasena(contrasena):
    print("La contraseña no es segura. Debe tener al menos 16 caracteres, incluir mayúsculas, minúsculas, números y caracteres especiales.")
    contrasena = generar_contrasena()
    print(f"Sugerencia de contraseña segura: {contrasena}")
print("La contraseña es segura.")