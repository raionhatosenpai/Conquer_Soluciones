# 1. Define una función llamada "saludar" que tome un parámetro "nombre"
# y muestre un saludo personalizado.

def saludar(nombre):
    print("¡Hola, " + nombre + "! Bienvenid@.")
# Ejemplo de uso
saludar("Ana")
saludar("Luis")
print("-" * 30)
# 2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
# imprima la suma de ambos.

def suma(a, b):
    print("La suma de " + str(a) + " y " + str(b) + " es: " + str(a + b))

# Ejemplo de uso
suma(5, 10)
suma(3.5, 2.5)
print("-" * 30)

# 3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
# parámetros "base" y "altura" y calcule el área de un rectángulo.

def calcular_area_rectangulo(base, altura):
    area = base * altura
    print("El área del rectángulo de base " + str(base) + " y altura " + str(altura) + " es: " + str(area))

# Ejemplo de uso
calcular_area_rectangulo(5, 10)
calcular_area_rectangulo(3.5, 2.5)
print("-" * 30)

# 4. Define una función llamada "imprimir_lista" que tome una lista como
# parámetro y la imprima en la consola.

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# Ejemplo de uso
imprimir_lista([1, 2, 3, 4, 5])
imprimir_lista(["a", "b", "c"])
print("-" * 30)

# 5. Crea una función llamada "es_par" que tome un número como
# parámetro e imprima True si es par, o False si es impar.

def es_par(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)

# Ejemplo de uso
print("el número " + str(4) + " es par?")
es_par(4)  # True
print("el número " + str(7) + " es par?")
es_par(7)  # False
print("-" * 30)

# 6. Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y "cadena2" e imprima la concatenación de
# ambas cadenas.

def concatenar_strings(cadena1, cadena2):
    print(cadena1 + cadena2)

# Ejemplo de uso
concatenar_strings("Hola, ", "mundo!")
concatenar_strings("Python ", "es genial.")
print("-" * 30)

# 7. Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.

def obtener_maximo(lista):
    if not lista:
        return None
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Ejemplo de uso
print(obtener_maximo([1, 2, 3, 4, 5]))
print(obtener_maximo([-1, -2, -3, -4, -5]))
print(obtener_maximo([]))
print("-" * 30)

# 8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.

def convertir_fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso
print(f"{convertir_fahrenheit_a_celsius(32):.2f} Grados Celsius")
print(f"{convertir_fahrenheit_a_celsius(100):.2f} Grados Celsius")
print("-" * 30)

# 9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad de una persona.

def calcular_edad(año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

# Ejemplo de uso
print(calcular_edad(2025, 1991))
print(calcular_edad(2025, 1997))
print("-" * 30)

# 10. Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor", o
# False si no lo es

def es_divisible(num, divisor):
    if divisor == 0:
        print("División por cero no permitida.")
    elif num % divisor == 0:
        print(True)
    else:
        print(False)

# Ejemplo de uso
print("¿Es divisible 10 entre 2?")
es_divisible(10, 2)  # True
print("¿Es divisible 10 entre 3?")
es_divisible(10, 3)  # False
print("¿Es divisible 10 entre 0?")
es_divisible(10, 0)  # División por cero no permitida.
print("-" * 30)

# 11. Crea una función llamada "mostrar_info_persona" que tome tres
# argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
# debe imprimir en la consola la información de una persona en un
# formato legible.

def mostrar_info_persona(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

# Ejemplo de uso
mostrar_info_persona(nombre="Alice", edad=30, ciudad="Bordeaux")
mostrar_info_persona(nombre="Bob", edad=25, ciudad="Madrid")
mostrar_info_persona(nombre="Charlie", edad=35, ciudad="Las Palmas de Gran Canaria")
print("-" * 30)

# 12. Escribe una función llamada "calcular_promedio" que tome una lista de
# números como parámetro y calcule el promedio de esos números. Si no
# se proporciona una lista, debe usar una lista vacía por defecto.

def calcular_promedio(numeros=None):
    if numeros is None:
        numeros = []
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# Ejemplo de uso
print(calcular_promedio([10, 20, 30, 40, 50]))
print(calcular_promedio([5, 15, 25, 35, 45]))
print(calcular_promedio())
print("-" * 30)

# 13. Crea una función llamada "calcular_potencia" que tome dos
# parámetros "base" y "exponente", y calcule la potencia de la base
# elevada al exponente. Utiliza 2 como valor por defecto para el
# exponente.

def calcular_potencia(base, exponente=2):
    return base ** exponente

# Ejemplo de uso
print(calcular_potencia(3)) # 3 elevado a la 2
print(calcular_potencia(4, 3)) # 4 elevado a la 3, sobrescribe el valor por defecto
print(calcular_potencia(5, 0)) # 5 elevado a la 0, cualquier número elevado a 0 es 1
print("-" * 30)

# 14. Define una función llamada "imprimir_info_alumno" que tome un
# argumento posicional “nombre”(y sin valor por defecto) y varios
# argumentos de palabra clave: "edad", "curso" y “promedio" (puedes
# ponerles como valor por defecto None). La función debe imprimir la
# información del alumno en un formato legible.

def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print(f"Nombre: {nombre}")
    if edad is not None:
        print(f"Edad: {edad}")
    if curso is not None:
        print(f"Curso: {curso}")
    if promedio is not None:
        print(f"Promedio: {promedio}")
    print("-" * 30)

# Ejemplo de uso
imprimir_info_alumno("Alice", 20, "Matemáticas", 9.5)
imprimir_info_alumno("Bob", 22, "Historia", 8.7)
imprimir_info_alumno("Charlie", 23, "Ciencias", 8.0)
imprimir_info_alumno("Diana")  # Solo nombre, otros valores por defecto
