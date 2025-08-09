# crear un  script para que imprima todos los numeros primos entre el 2 y el 100
for i in range(2, 101):
    es_primo = True # definimos una variable para saber si es primo

    # comprobamos si es primo, si es divisible por otro numero que no sea 1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:# si es divisible por otro numero que no sea 1 o el mismo, no es primo
            es_primo = False # si es divisible, no es primo y cambiamos la variable a False
            break
    if es_primo: # si es primo, lo imprimimos
        print(i, end='  ') # imprimimos el numero primo y un espacio en blanco al final
        
# Este script imprimirá todos los números primos entre 2 y 100, separados por espacios.
# Ejemplo de salida:
    # Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97