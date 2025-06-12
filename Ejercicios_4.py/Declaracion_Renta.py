# realizar un script que calcule la declaracion de la renta de un trabajador segun su edad y salario
# Si el trabajador tiene menos de 18 años o un salario mensual inferior a 1000 euros, no se aplica impuesto.
# Si cumple con los requisitos, se calcula la renta anual y se aplica un tipo impositivo según tramos.
# Los tramos son:
# - Menos de 15,000 euros: 5%
# - Entre 15,000 y 25,000 euros: 15%
# - Entre 25,000 y 35,000 euros: 20%
# - Entre 35,000 y 60,000 euros: 30%
# - Más de 60,000 euros: 45%
# El script imprime el impuesto a pagar y la renta anual del trabajador.

edad = int(input("\nIngrese su edad: "))
salario = float(input("\nIngrese su salario mensual: "))
renta_anual = salario * 12
if edad >= 18 and salario >= 1000:
    if renta_anual <= 15000:
        impuesto = renta_anual * 0.05
        print(f"\nCon una renta anual de {renta_anual:.2f} euros, el tipo impositivo es del 5%.")
    elif renta_anual <= 25000:
        impuesto = renta_anual * 0.15
        print(f"\nCon una renta anual de {renta_anual:.2f} euros, el tipo impositivo es del 15%.")
    elif renta_anual <= 35000:
        impuesto = renta_anual * 0.20
        print(f"\nCon una renta anual de {renta_anual:.2f} euros, el tipo impositivo es del 20%.")
    elif renta_anual <= 60000:
        impuesto = renta_anual * 0.30
        print(f"\nCon una renta anual de {renta_anual:.2f} euros, el tipo impositivo es del 30%.")
    else:
        impuesto = renta_anual * 0.45
        print(f"\nCon una renta anual de {renta_anual:.2f} euros, el tipo impositivo es del 45%.")
else:
    impuesto = 0
    print("\nNo se aplica impuesto. Debes tener al menos 18 años y un salario mensual superior a 1000 euros.")
print(f"\nEl impuesto a pagar es de {impuesto:.2f} euros.")
print("\nGracias por utilizar el sistema de declaración de la renta.")
print("\n-" * 5) # Cierre del script algo mas visual
# Este script calcula la declaración de la renta de un trabajador según su edad y salario mensual.        
