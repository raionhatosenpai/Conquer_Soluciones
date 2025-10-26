''' Estás desarrollando un sistema de autenticación para una aplicación web y 
deseas implementar un sistema de inicio de sesión que verifique si las 
credenciales proporcionadas por el usuario son válidas antes de permitir el 
acceso a ciertas funciones. 

Además, deseas que una vez que el usuario haya 
iniciado sesión correctamente, se le proporcione información personal.
 
Implementa lo siguiente:

1. Un registro de usuarios que contenga información adicional, como el 
nombre completo y el correo electrónico.

2. Un decorador llamado 
verificar_inicio_sesion que acepte el nombre de 
usuario y la contraseña como argumentos. Este decorador verificará si las 
credenciales proporcionadas son válidas comparándolas con el registro de 
usuarios. Si las credenciales son válidas, la función decorada se ejecutará y 
se le pasará como argumento la información personal del usuario.

3. Una función llamada 
informacion_usuario que imprima la información personal 
del usuario después de que haya iniciado sesión correctamente.

Implementa este sistema de inicio de sesión utilizando decoradores'''

# Registro de usuarios con información adicional
registro_usuarios = {
  "raionhato": {
    "password": "1234",
    "nombre": "Luis Carlos Quinchía",
    "correo": "raionhato@ejemplo.com"
    },
    "admin": {
    "password": "adminpass",
    "nombre": "Administrador",
    "correo": "admin@ejemplo.com"
    }
}

# Decorador para verificar el inicio de sesión
def verificar_inicio_sesion(usuario, contrasena):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            if usuario in registro_usuarios and registro_usuarios[usuario]["password"] == contrasena:
                print("✅ Inicio de sesión exitoso.")
                info_personal = {
                    "nombre": registro_usuarios[usuario]["nombre"],
                    "correo": registro_usuarios[usuario]["correo"]
                }
                return funcion(info_personal, *args, **kwargs)
            else:
                print("⛔ Credenciales inválidas. Acceso denegado.")
        return wrapper
    return decorador

# Función para mostrar la información del usuario
def informacion_usuario(info_personal):
    print(f"👤 Información del Usuario:")
    print(f"Nombre: {info_personal['nombre']}")
    print(f"Correo: {info_personal['correo']}")

# Ejemplo de uso
while True:
    print("\n--- Sistema de Inicio de Sesión ---")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
     # Aplicamos el decorador con los datos proporcionados
    decorada = verificar_inicio_sesion(usuario, contrasena)(informacion_usuario)
    decorada()  # Llamamos la función decorada
    continuar = input("¿Desea intentar iniciar sesión nuevamente? (s/n): ")
    if continuar.lower() != 's':
        print("Saliendo del sistema de inicio de sesión.")
        break