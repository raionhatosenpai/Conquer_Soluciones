
# Validar entrada
while True: # while (mientras) para repetir hasta que se cumpla la condición
    cadena = input("Intoduce 5 caracteres: ")
    if len(cadena) == 5:  # verificar longitud
        break
    else:
        print("❌ Número inválido. Asegúrate de introducir 5 caracteres.")  # Mensaje de error

caracter_nuevo = "" # Inicializar variable para almacenar el nuevo carácter
for caracter in cadena: # recorrer cada carácter en la cadena
    # Duplicar cada carácter
    caracter_nuevo += caracter + caracter

print("Resultado:", caracter_nuevo)# Imprimir el resultado final