# pedir una frase y una letra y contar cuántas veces aparece la letra en la frase
frase = input("Introduce una frase: ").strip().lower()
letra = input("Introduce una letra: ").strip().lower()
contador = 0
# bucle for para recorrer cada carácter de la frase
for caracter in frase:
    # Si el carácter es igual a la letra, incrementar el contador
    if caracter == letra:
        contador += 1
# Imprimir el resultado
print(f"La letra '{letra.upper()}' aparece {contador} veces en la frase.")
# Imprimir una nueva línea al final
print()