# FACTORIAL 
# Implementa una función recursiva llamada factorial que calcule el factorial de 
# un número entero positivo. El factorial de un número n se define como el 
# producto de todos los números enteros positivos desde 1 hasta n.
# (El factorial de 0 y de 1 es igual a 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Ejemplo de uso:
numero = 5  
print(f"El factorial de {numero} es {factorial(numero)}")
# Ejemplo de uso:   
numero = 0  
print(f"El factorial de {numero} es {factorial(numero)}")
