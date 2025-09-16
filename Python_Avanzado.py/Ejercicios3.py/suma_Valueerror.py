# Escribe un programa que solicite dos números.
# Suma los números y muestra el resultado. Captura el 
# ValueError si alguno de los valores de entrada no es un número e imprime un 
# mensaje de error amigable. Prueba tu programa ingresando dos números y 
# luego ingresando texto en lugar de un número. Envuelve tu código del en un 
# bucle while para que el usuario pueda continuar ingresando números incluso 
# si comete un error ingresando texto en lugar de un número.


# Sumar N° y mostrar resultado
def suma_numeros():
    while True:
        try:
            num1 = float(input("Introduzca el PRIMER digito: "))
            num2 = float(input("Introduzca el SEGUNDO digito: "))
        except ValueError:
            print("Error: Por favor, ingrese solo números válidos.")
        else:
            resultado = num1 + num2
            print(f"La suma de {num1} y {num2} es: {resultado}")
            break

suma_numeros()