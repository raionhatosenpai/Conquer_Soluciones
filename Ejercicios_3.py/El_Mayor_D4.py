# El mayor de 4 numeros

# solicitar 4 numeros al usuario
num1 = int(input("\nIngrese el primer numero: "))
num2 = int(input("\nIngrese el segundo numero: "))
num3 = int(input("\nIngrese el tercer numero: "))
num4 = int(input("\nIngrese el cuarto numero: "))

# encontrar el mayor de los 4 numeros
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
if num4 > mayor:
    mayor = num4

# mostrar el resultado
print(f"\nEl mayor de los 4 numeros {num1}, {num2}, {num3}, {num4} es: {mayor}")
