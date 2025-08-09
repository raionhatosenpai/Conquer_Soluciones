# Importar módulos de expresiones regulares
import re # Importar el módulo re para expresiones regulares

# Definir Usuarios válidos para el mensaje de bienvenida
usuarios_Validos = {"Alejandro", "Naomi", "Sergio", "Luis"}

    # Solicitar nombre de usuario
usuario = str(input("¿Quien esta hay? "))
    # Limpiar el nombre de usuario
usuario_Limpio = re.sub(r"[^a-zA-Z]", "", usuario).title() # Eliminar caracteres no alfabéticos y capitalizar
    # Verificar si el usuario ya existe
if usuario_Limpio not in usuarios_Validos:
        print(f"Bienvenido, {usuario_Limpio}") # con f-string puedo concatenar variables en un string 
else: 
        # Si el usuario ya existe, mostrar un mensaje de bienvenida
        print(f"Bienvenid@, {usuario_Limpio}, te estaba esperando, crack!")
        print(f"Eres de los nuestros, de los real")
        print(f"Eres un genio")
        print(f"Eres un artista")
        print(f"Eres un maestro")
        print(f"Eres un campeón")
        print(f"Eres un fenómeno")
