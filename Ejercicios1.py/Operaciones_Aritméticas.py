# Operaciones A
resultado = ((3+2)/(2*5))**2
print("el resultado de la operación ((3+2)/(2*5))**2 es: ", round(resultado, 2)) # round() redondea el resultado a 2 decimales

# Operaciones B
print("\nOperacion B")
numero = int(input("Introduce un número entero: "))
while numero <= 0:
    print("❌ Número inválido. Asegúrate de introducir un número entero positivo.")  # Mensaje de error
    numero = int(input("Introduce un número entero: ")) # permite volver a introducir el número
resultado_b =  numero * (numero + 1) / 2 # Fórmula de la suma de los primeros n números enteros
print(f"La suma de los primeros {numero} números enteros es: {resultado_b}")

# Operaciones C
print("\nOperacion C")
digito_1 = int(input("Introduce un número entero: "))
digito_2 = int(input("Introduce otro número entero: "))

while digito_2 == 0: # Validar entrada
    print("❌ Número inválido. Asegúrate de introducir un número entero diferente de cero.")  # Mensaje de error
    digito_2 = int(input("Introduce otro número entero diferente de cero: ")) # permite volver a introducir el número
# realizar la división y el resto
cociente = digito_1 // digito_2
resto = digito_1 % digito_2
# Imprimir el resultado
print(f"El cociente de {digito_1} entre {digito_2} es: {cociente}, y el resto es: {resto}")