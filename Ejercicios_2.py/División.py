# con try-except para manejar errores de entrada y división por cero
# Ejercicio de división con manejo de errores

# Solicitar dos números para realizar una división
try:
    dividendo = float(input("\nIntroduce el dividendo: "))
    divisor = float(input("\nIntroduce el divisor: "))

    resultado = dividendo / divisor
    print(f"\nEl resultado de la división es: {round(resultado, 2)}")

 # Manejar errores de entrada no numérica
except ValueError:
    print("\nError: Entrada no válida. Por favor, introduce números.")

 # Manejar errores de división por cero
except ZeroDivisionError:
    print("\nError: División por cero no permitida. Por favor, introduce un divisor diferente de cero.")