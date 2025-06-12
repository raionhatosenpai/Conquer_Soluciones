# Establecer la password de un usuario
password = "Python123"
# Solicitar al usuario que introduzca su password
user_input = str(input("\nIntroduce tu password: "))
# Comprobar si la password introducida es correcta teniendo en cuenta errores
user_input_limpio = (f"{user_input.strip().replace(' ', '').lower()}")
# Podriamos usar: user_input_limpio = re.sub(r"[^a-zA-Z0-9]", "", user_input).lower() para eliminar caracteres no alfanuméricos-
# y convertir a minúsculas 
password_limpio = (f"{password.strip().replace(' ', '').lower()}")
if user_input_limpio == password_limpio:
    print("\nPassword correcta")
else:
    user_input_2 = str(input("\nPassword incorrecta. Por favor, inténtalo de nuevo: "))
    user_input_2_limpio = (f"{user_input_2.strip().replace(' ', '').lower()}")
    password_limpio = (f"{password.strip().replace(' ', '').lower()}")
    if user_input_2_limpio == password_limpio:
        print("\nPassword correcta")
    else:
        print("\nPassword incorrecta. Has agotado tus intentos.")
        exit()