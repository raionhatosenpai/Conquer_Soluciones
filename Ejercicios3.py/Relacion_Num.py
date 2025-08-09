# RELACION ENTRE NÚMEROS:
# Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
# de los otros dos.

# Solicitar 3 números diferentes al usuario
num1 = int(input("\nIngrese el primer número: "))
num2 = int(input("\nIngrese el segundo número: "))
num3 = int(input("\nIngrese el tercer número: "))

# Verificar que los números son diferentes
if num1 == num2 or num1 == num3 or num2 == num3:
    print("\nLos números deben ser diferentes. Por favor, intente de nuevo.")
    exit()
# Verificar si alguno de los números es la suma de los otros dos
if num1 == num2 + num3:
    print(f"\nEl primer número ({num1}) es la suma de los otros dos ({num2} y {num3}).")
elif num2 == num1 + num3:
    print(f"\nEl segundo número ({num2}) es la suma de los otros dos ({num1} y {num3}).")
elif num3 == num1 + num2:
    print(f"\nEl tercer número ({num3}) es la suma de los otros dos ({num1} y {num2}).")
else:
    print(f"\nNinguno de los números ({num1}, {num2}, {num3}) es la suma de los otros dos.")