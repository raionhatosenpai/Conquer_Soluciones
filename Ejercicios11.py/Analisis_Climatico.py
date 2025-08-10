# Ejercicio: Análisis Climático

import numpy as np

clima = np.array([
                   [20, 70, 1009, 1],
                   [22, 65, 1010, 2],
                   [21, 75, 1008, 3],
                   [19, 80, 1007, 4],
                   [23, 60, 1011, 5],
                   [24, 55, 1012, 6],
                   [25, 50, 1013, 7],
                   [26, 45, 1014, 8],
                   [27, 40, 1015, 9],
                   [28, 35, 1016, 10],
                   [29, 30, 1017, 11],
                   [30, 25, 1018, 12],
                   [31, 20, 1019, 1],
                   [32, 15, 1020, 5],
                   [33, 10, 1021, 1],
                   [34, 5, 1022, 7],
                   [35, 0, 1023, 10],
                   [18, 85, 1005, 2],
                   [19, 80, 1006, 4],
                   [20, 75, 1007, 6],
                   [21, 70, 1008, 8],
                   [22, 65, 1009, 10],
                   [23, 60, 1010, 12],
                   [24, 55, 1011, 1],
                   [25, 50, 1012, 3],
                   [26, 45, 1013, 5],
                   [27, 40, 1014, 7],
                   [28, 35, 1015, 9],
                   [29, 30, 1016, 11],
                   [30, 25, 1017, 1],
                   [31, 20, 1018, 5],
                   [32, 15, 1019, 1],
                   [33, 10, 1020, 7],
                   [34, 5, 1021, 10],
                   [35, 0, 1022, 12],
                   [18, 85, 1005, 2],
                   [19, 80, 1006, 4],])

# usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde n es el número de mediciones.
clasificaciones = np.add(clima[:, :3], 0)  # Crea un array de las primeras tres columnas (temperatura, humedad, presión)

# filtrar los datos por mes y calcular las medias de temperatura, humedad y presión atmosférica correspondientes
meses = clima[:, 3]  # Extrae la columna de meses
temperatura = clima[:, 0] # Extrae la columna de temperatura
humedad = clima[:, 1] # Extrae la columna de humedad
presion = clima[:, 2] # Extrae la columna de presión
temp_mes = np.zeros(12) 
hum_mes = np.zeros(12)
pres_mes = np.zeros(12)

# calcular las medias por mes
for i in range(12):

   temp_mes[i] = np.mean(temperatura[meses == i+1])
   humedad[i] = np.mean(humedad[meses == i+1])
   presion[i] = np.mean(presion[meses == i+1])


   print("Temperatura media del mes", i+1, "fue de: ---->>", temp_mes[i].round(2))
   print("Humedad media del mes", i+1, "fue de: ----->>", humedad[i].round(2))
   print("Presión media del mes", i+1, "fue de: ----->>", presion[i].round(2))
   print(" ")