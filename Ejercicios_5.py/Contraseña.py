Clave_Secreta = "MiContraseña123"
while True:
    Contraseña = input("Introduce la contraseña: ")
    if Contraseña == Clave_Secreta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")