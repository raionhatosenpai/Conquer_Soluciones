# Version 2: Mejorada con manejo de excepciones

# Defino una función para encontrar el mayor de 4 números ingresados por el usuario
def encontrar_mayor(numeros):
    mayor = numeros[0]
    for num in numeros[1:]:
        if num > mayor:
            mayor = num
    return mayor

# Solicitar 4 números al usuario y manejar excepciones
numeros = []
for i in range(4): # crear bucle para solicitar 4 números
    while True: # bucle para asegurar que se ingrese un número válido
        try: # intentar convertir la entrada a un número entero
            num = int(input(f"\nIngrese el número {i + 1}: "))
            numeros.append(num)
            break
        except ValueError: # manejar el caso en que la conversión falle
            print("\nEntrada inválida. Por favor, ingrese un número entero.")

mayor = encontrar_mayor(numeros) # Llamar a la función para encontrar el mayor número

# Mostrar el resultado
print("\nEl mayor de los 4 números es:", mayor)