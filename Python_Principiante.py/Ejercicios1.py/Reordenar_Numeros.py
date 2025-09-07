# Solicita al usuario un número de más de una cifra
numero = input("Ingrese un número de mas de una cifra: ")

# Validar que el número ingresado sea de mas de una cifra
if len(numero) > 1 : #Uso len() para verificar la longitud del número
# Reordenar los dígitos del número
    for num in str(numero): #for num in str(numero) convierte el número en una cadena para poder iterar sobre sus dígitos
      print (num)
else: # si el número tiene menos de dos cifras, dara este mensaje
    print("El número ingresado no es válido. Debe tener más de una cifra.")

# Invierto el número
numero_invertido = numero[::-1] #[::-1] es una forma de invertir una cadena en Python, toma el ultimo carácter y lo coloca al principio,
# el penúltimo al segundo lugar, y así sucesivamente.
print("El número invertido es:", numero_invertido) #imprime el número invertido