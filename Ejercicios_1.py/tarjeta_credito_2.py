# Validar entrada
while True:
    numero_tarjeta = input("Introduce el número de tarjeta (16 dígitos, con o sin espacios): ")
    numero_limpio = numero_tarjeta.replace(" ", "") # eliminar espacios
    
    if len(numero_limpio) == 16 and numero_limpio.isdigit(): # verificar longitud y si es numérico
        break
    else:
        print("❌ Número inválido. Asegúrate de introducir 16 dígitos numéricos.") # Mensaje de error

# Dar formato a bloques de 4 si no lo trae
if " " not in numero_tarjeta: # si no tiene espacios
    bloques = [numero_limpio[i:i+4] for i in range(0, 16, 4)] # dividir en bloques de 4
else:
    bloques = numero_tarjeta.split(" ") # añadir espacios

# Ocultar todos menos el último
for t in range(len(bloques) - 1):
    bloques[t] = "****"

# Unir bloques en una cadena y mostrar el número oculto
numero_oculto = " ".join(bloques)
print(f"🔐 El número de tarjeta es: {numero_oculto}")
