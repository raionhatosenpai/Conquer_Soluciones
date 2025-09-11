#SUMA ELEMENTOS DE UNA LISTA 
# Crea una función recursiva llamada suma_lista que calcule la suma de todos 
# los elementos de una lista de enteros. Puedes asumir que la lista no está vacía.  

def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])
# Ejemplo de uso:   
mi_lista = [1, 2, 3, 4, 5]
print(f"La suma de los elementos de la lista {mi_lista} es {suma_lista(mi_lista)}")
# Ejemplo de uso:
mi_lista = [10]
print(f"La suma de los elementos de la lista {mi_lista} es {suma_lista(mi_lista)}")