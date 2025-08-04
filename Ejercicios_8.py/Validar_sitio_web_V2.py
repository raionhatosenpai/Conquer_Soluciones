# Supongamos que estos son los credenciales correctos
nombres_contraseñas = [["juan123", "clave123"], ["ana456", "clave456"], ["pedro789", "clave789"]]

# Verifica si el nombre de usuario y la contraseña coinciden con los de la lista permitiendo 2 intentos
intentos = 0
max_intentos = 2

while intentos < max_intentos:
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if [nombre_usuario, contrasena] in nombres_contraseñas:
        print("✅ Acceso concedido.")
        break
    else:
        print("❌ Acceso denegado.")
        intentos += 1

if intentos == max_intentos:
    print("🔒 Has excedido el número máximo de intentos.")

# es recomendable evitar repetir input() al principio fuera del bucle,
# ya que ya lo estás manejando dentro del while.
# Ventajas de esta versión:
# 1º El bucle es más compacto.
# 2º Evita duplicación de código (input()).
# 3º El mensaje de fallo final queda fuera del bucle para mayor claridad.