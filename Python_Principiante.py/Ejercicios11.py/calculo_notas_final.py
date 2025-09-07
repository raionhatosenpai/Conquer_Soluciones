# tienes un conjunto de calificaciones de un grupo de estudiantes en un curso, Cada estudiante tiene cuatro calificaciones: dos exámenes, 
# un trabajo final y una participación en clase Quieres calcular la nota final de cada estudiante, donde los
# exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase vale un 10%.
# Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, donde n es el número de estudiantes. Cada columna representa una de las calificaciones
# y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola columna.

import numpy as np

# crear un array de 4 columnas y n filas, donde n es el número de estudiantes
alumnos = int(input("Introduce la cantidad de alumnos: "))
calificaciones = np.zeros((alumnos, 4))

for i in range(alumnos):
    print(f"Introduce las calificaciones del alumno {i + 1}:")
    for j in range(4):
        calificaciones[i, j] = float(input(f"Calificación {j + 1}: "))

print("-------------------------------------------------------------------")

# calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola columna
if alumnos <= 0:
      print("No hay alumnos para calcular notas.")
else:
    notas_finales = np.sum(calificaciones * np.array([0.3, 0.3, 0.3, 0.1]), axis=1)
    for a in range(alumnos):
        print(f"La nota final del alumno {a + 1} es: {notas_finales[a]}")
print("-------------------------------------------------------------------")