# pedir un palabra y mostrarla al revés
palabra = input("Introduce una palabra: ")
# Invertir la palabra
# bucle for para recorrer la palabra al revés empezando por el último carácter
for i in range(len(palabra) - 1, -1, -1):
    # Imprimir cada carácter de la palabra al revés
    print(palabra[i], " ", end="")
print()  # Para añadir una nueva línea al final