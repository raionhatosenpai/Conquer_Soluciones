# pedir el nº de tarjeta
numero_tarjeta = input("Introduce el número de tarjeta: ")

# dividir el nº de tarjeta en 4 bloques de 4 dígitos
bloques = numero_tarjeta.split(" ") 

# t = tarjeta
for t in range(len(bloques) -1): #se recorre la lista de bloques menos el último
    bloques[t] = "****" #se ocultan los bloques de la tarjeta excepto el último
numero_oculto = " ".join(bloques) #se unen los bloques de la tarjeta en una sola cadena

print(f"El número de tarjeta es: {numero_oculto}") #se imprime el nº de tarjeta oculto