# solicitar Nº base y un Nº para la potencia
base = int(input("\nIntroduce un número base: "))
exponente = int(input("\nIntroduce un número para la potencia: "))

# calcular la potencia
resultado = base ** exponente

# mostrar el resultado
print(f"\nEl resultado de {base} elevado a {exponente} es: {resultado}")

# Comprobar si el resultado es par o impar
if resultado % 2 == 0:
    print(f"\nEl resultado {resultado} es un número par.")
else:
    print(f"\nEl resultado {resultado} es un número impar.")