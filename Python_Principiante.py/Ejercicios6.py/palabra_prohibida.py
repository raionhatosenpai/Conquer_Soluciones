# Define una lista de 5 palabras aleatorias
palabras = ["python", "programacion", "ejercicio", "desarrollo", "aprendizaje"]
print("Lista original de strings:", palabras)

#  una lista de letras prohibidas que contenga tres letras
letras_prohibidas = ['a', 'n', 'h']

# Filtra las palabras en tu lista original
palabras_permitidas = []
for palabra in palabras:
    if not any(letra in palabra for letra in letras_prohibidas):
        palabras_permitidas.append(palabra)
        print("Palabra permitida:", palabras_permitidas)