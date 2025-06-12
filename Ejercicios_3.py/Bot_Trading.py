# Objetivo del ejercicio
# Debes crear un script que simule el comportamiento de un bot de trading basado en el precio de un producto financiero. 
# El usuario introduce el precio, y según ese valor el bot decide qué hacer.

# Convertir el precio a float y manejar errores si el usuario introduce texto no numérico
try:
    precio = float(input("\nIntroduce el precio del producto financiero que deseas analizar: "))
    if precio < 100:
        print("\nEl bot decide comprar.")# Decisión del bot basada en el precio
    elif 100 <= precio < 150:
        print("\nEl bot decide mantener la posición.")# Decisión del bot basada en el precio
    else:
        print("\nEl bot decide vender.") # Decisión del bot basada en el precio
    print("Orden ejecutado con éxito.")# Mensaje de éxito al ejecutar la orden
except ValueError:
    print("\nEntrada inválida. Por favor, introduce un número válido para el precio.")# Manejo de errores para entradas no numéricas