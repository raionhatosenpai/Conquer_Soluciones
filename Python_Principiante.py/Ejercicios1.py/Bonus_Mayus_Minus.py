# Crear un script que permita al usuario introducir una sola letra, y luego determine si es mayúscula o minúscula.

# Solitamos al usuario que introduzca una letra
letra = input("\nIntroduce una letra: ")

if len(letra) == 1 and letra.isalpha(): # Verificamos que la entrada sea una sola letra y que sea alfabética
    if letra.isupper(): # Verificamos si la letra es mayúscula
      print("\nLa letra es mayúscula.")
    else: # Si no es mayúscula, entonces es minúscula
      print("\nLa letra es minúscula.")
else: # Si la entrada no es válida, mostramos un mensaje de error
    print("\nEntrada inválida. Por favor, introduce una sola letra.")