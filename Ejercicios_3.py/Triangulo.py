#  Objetivo del ejercicio
# Determinar si tres longitudes dadas pueden formar un triángulo.

# Solititamos al usuario que ingrese las longitudes de los lados del triángulo
lados = []  # Lista para almacenar las longitudes de los lados
for i in range(3):
    while True:  # Bucle para asegurar que se ingrese un número válido
        try:
            lado = float(input(f"\nIngrese la longitud del lado {i + 1} del triángulo: "))
            if lado <= 0:  # Verificar que el lado sea positivo
                print("\nLa longitud debe ser un número positivo. Inténtalo de nuevo.")
            else:
                lados.append(lado)  # Agregar el lado a la lista
                break  # Salir del bucle si la entrada es válida
        except ValueError:  # Manejar el caso en que la conversión falle
            print("\nEntrada inválida. Por favor, ingrese un número válido.")

# Comprobar si las longitudes pueden formar un triángulo
if (lados[0] + lados[1] > lados[2]) and (lados[0] + lados[2] > lados[1]) and (lados[1] + lados[2] > lados[0]):
    print(f"\nSí, con las longitudes {lados[0]}, {lados[1]} y {lados[2]} se puede formar un triángulo.")
else:
    print(f"\nNo, con las longitudes {lados[0]}, {lados[1]} y {lados[2]} no se puede formar un triángulo.")

