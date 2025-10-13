'''Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres 
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos 
apilados en orden descendente, desde el disco N en la parte inferior hasta el 
disco 1 en la parte superior.

Tu tarea es implementar una solución recursiva para mover todos los discos 
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de 
Hanoi:
- Puedes mover un disco a una torre adyacente.
- Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si 
el disco superior es más grande que el disco que estás colocando.

Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar) que,
dado el número total de discos n y las torres de origen, destino y auxiliar, 
imprima los pasos necesarios para lograr el movimiento de todos los discos 
desde la torre A hasta la torre C'''

def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de la torre {origen} a la torre {destino}")
        return
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de la torre {origen} a la torre {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso
torres_de_hanoi(5, 'A', 'C', 'B')

# Puede probar con diferentes valores de n para ver cómo se resuelve el problema
# incluso utilizar buclues para probar con varios valores de n, o interactuar con el usuario
# para que ingrese el número de discos, el origen, destino y auxiliar.