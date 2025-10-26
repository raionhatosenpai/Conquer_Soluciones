''' Imagina que eres parte de un equipo de desarrollo de IA que se encarga de 
crear un sistema para que un robot resuelva laberintos. El laberinto está 
representado por una matriz, donde ciertos valores indican:
caminos permitidos (0), paredes (1), y la salida (9).

Tu tarea es implementar una función recursiva que encuentre la ruta más corta
para que el robot salga del laberinto.

Toma en cuenta los siguientes puntos:
 - La matriz representa el laberinto, donde los valores son:
 0 : Camino permitido.
 1 : Pared, no se puede atravesar.
 9 : Salida del laberinto.

- Debes implementar la función resolver_laberinto que utiliza recursividad 
para encontrar la ruta más corta desde una posición inicial hasta la salida.

- La función debe devolver una lista de coordenadas que representan la ruta 
desde la posición inicial hasta la salida.

- Puedes usar una lista de movimientos posibles: 
 arriba ((-1, 0) ),
 abajo ((1, 0) ),
 izquierda ((0, -1) ), 
 derecha ((0, 1) ).'''

def resolver_laberinto(laberinto,fila,columna,camino=None):
  if camino is None:
    camino = []

  if not(0<=fila<len(laberinto)) or not (0<=columna<len(laberinto[0])) or laberinto[fila][columna]==1 or (fila,columna) in camino:
    return None
  camino.append((fila,columna))

  #caso base ///// si ya nos enconotramos la salida

  if laberinto[fila][columna]==9:
    return camino

  #definir los movimientos posibles
  movimientos=[(-1,0),(1,0),(0,-1),(0,1)]

  for movimiento in movimientos:
    nueva_fila,nueva_columna=fila+movimiento[0],columna+movimiento[1]
    resultado = resolver_laberinto(laberinto,nueva_fila,nueva_columna,camino.copy())
    if resultado:
      return resultado
  return None # No hay una solucion desde esta posicion.

def imprimir_laberinto(laberinto,camino):
  for fila in range(len(laberinto)):
    for columna in range(len(laberinto[0])):
      if (fila,columna) in camino:
        print("*",end=" ") #Representa el camino

      else:
        valor = laberinto[fila][columna]
        if valor == 1:
            print("█", end=" ")
        elif valor == 9:
            print("🏁", end=" ")
        else:
            print("%", end=" ")
    print()

laberinto = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 9, 0, 0, 0, 0, 0]
]
camino_solucion = resolver_laberinto(laberinto,0,0)

if camino_solucion:
  print("El camino para salir del laberinto es:")
  imprimir_laberinto(laberinto,camino_solucion)
else:
  print('No hay solucion para este laberinto')
