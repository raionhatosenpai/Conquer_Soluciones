# NUMERO TRIANGULAR 
# Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
# número triangular. Un número triangular se obtiene al sumar todos los 
# números naturales desde 1 hasta n

def numero_triangular(n):
    # Caso base: si n es 1, el número triangular es 1
    if n == 1:
        return 1
    else:
        # Llamada recursiva: n + numero_triangular(n - 1)
        return n + numero_triangular(n - 1)
    
# Ejemplo de uso
print(numero_triangular(5))  # Salida: 15 (1 + 2 + 3 + 4 + 5 = 15)