# Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la venta y la categoría de producto vendido
# analizar estos datos para determinar cuánto fue el monto total de ventas en cada mes
# cargar los datos en un array de 3 columnas y n filas, donde n es el número de ventas
# puedes usar operaciones de NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes

import numpy as np

# cargar los datos en un array de 3 columnas y n filas, donde n es el número de ventas
ventas = np.array([
    ['2023-01-15', 100, 'Electrónica'],
    ['2023-01-20', 150, 'Ropa'],
    ['2023-02-10', 200, 'Electrónica'],
    ['2023-02-15', 250, 'Ropa'],
    ['2023-03-05', 300, 'Electrónica'],
    ['2023-03-10', 350, 'Ropa'],
    ['2023-04-16', 110, 'Alimentos'],
    ['2023-04-20', 130, 'Electrónica'],
    ['2023-04-25', 120, 'Ropa'],
    ['2023-04-30', 140, 'Alimentos']
])

# filtrar los datos por mes y sumar los montos de venta correspondientes
fecha = np.array([venta[0] for venta in ventas])
meses = np.array([int(fecha[5:7]) for fecha in fecha])

# calcular el monto total de ventas por mes
montos_mes = np.zeros(12)
for mes in range(1, 13):
    ventas_mes = ventas[meses == mes]
    montos_mes[mes - 1] = np.sum(ventas_mes[:, 1].astype(int))
print("Monto total de ventas por mes:", montos_mes)