# definir lista de números enteros
numeros = range(1, 21)

# escribe un script en Python que devuelva una nueva lista con los números primos de la lista original
si_primos = []
no_primos = []
for numero in numeros:
    es_primo = True  # asumimos que el número es primo
    if numero < 2:  # los números menores que 2 no son primos
        es_primo = False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:  # si es divisible por otro número, no es primo
                es_primo = False
                break
    if es_primo:
        si_primos.append(numero)  # añadimos a la lista de primos y los sumamos
        total_primos = len(si_primos)  # contamos los primos
        suma_primos = sum(si_primos)  # sumamos los primos
    else:
        no_primos.append(numero)  # añadimos a la lista de no primos y los sumamos
        total_no_primos = len(no_primos)  # contamos los no primos
        suma_no_primos = sum(no_primos)  # sumamos los no primos

# Imprimir resultados
print("Números primos:", si_primos)
print(f"Total de números primos: {total_primos} con una suma de {suma_primos}")
print("\n----------------------------")

# lo mismo para los no primos
print("Números no primos:", no_primos)
print(f"Total de números no primos: {total_no_primos} con una suma de {suma_no_primos}")
print("\n----------------------------")