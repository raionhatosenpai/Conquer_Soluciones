# Importar la librería de autenticación
import re
# Establecer la password de un usuario
password = "Python123"
# Solicitar al usuario que introduzca su password
user_input = str(input("\nIntroduce tu password: "))
# establecer un contador de intentos
intentos = 1
# Comprobar si la password introducida es correcta teniendo en cuenta errores
user_input_limpio = re.sub(r"[^a-zA-Z0-9]", "", user_input).lower()
password_limpio = re.sub(r"[^a-zA-Z0-9]", "", password).lower()
# creo un bucle para permitir varios intentos (Max 2)
# mientras la password introducida no sea igual a la password establecida
# y el número de intentos sea menor que 2
while not user_input_limpio == password_limpio and intentos < 2:
    # incrementar el contador de intentos
    intentos += 1
    # solicitar al usuario que introduzca su password de nuevo   
    user_input = str(input("\nHey! Colega parece que te has equivocado. Por favor, inténtalo de nuevo: "))
    user_input_limpio = re.sub(r"[^a-zA-Z0-9]", "", user_input).lower()
if user_input_limpio == password_limpio:
    print("\nPassword correcta, bienvenido al sistema, Buddy!")  # Si la password introducida es correcta, mostrar un mensaje de bienvenida
else:
    print("\nPassword incorrecta. Has agotado tus intentos.")  # Si la password introducida es incorrecta, mostrar un mensaje de error
    exit()  # Salir del programa si se han agotado los intentos