# Solicitar 3 números diferentes al usuario y manejar excepciones
def solicitar_numeros():
    numeros = []
    for i in range(3):  # crear bucle para solicitar 3 números
        while True:  # bucle para asegurar que se ingrese un número válido
            try:  # intentar convertir la entrada a un número entero
                num = int(input(f"\nIngrese el número {i + 1}: "))
                if num in numeros:  # verificar si el número ya fue ingresado
                    print("\nEl número ya ha sido ingresado. Por favor, ingrese un número diferente.")
                else:
                    numeros.append(num)
                    break
            except ValueError:  # manejar el caso en que la conversión falle
                print("\nEntrada inválida. Por favor, ingrese un número entero.")
    return numeros
# comprobar si alguno de los números es la suma de los otros dos
def verificar_suma(numeros):
    num1, num2, num3 = numeros
    if num1 == num2 + num3:
        return f"\nEl primer número ({num1}) es la suma de los otros dos ({num2} y {num3})."
    elif num2 == num1 + num3:
        return f"\nEl segundo número ({num2}) es la suma de los otros dos ({num1} y {num3})."
    elif num3 == num1 + num2:
        return f"\nEl tercer número ({num3}) es la suma de los otros dos ({num1} y {num2})."
    else:
        return f"\nNinguno de los números ({num1}, {num2}, {num3}) es la suma de los otros dos."
    
# Mostrar el resultado
numeros = solicitar_numeros()  # Llamar a la función para solicitar los números
resultado = verificar_suma(numeros)  # Llamar a la función para verificar la suma
print(resultado)  # Mostrar el resultado final