# Define dos listas Una con los valores de ventas por día (30 elementos).
ventas_por_dia = [100, 200, 150, 300, 250, 400, 350, 450, 500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050, 1200, 1150, 1300, 1250, 1400, 1350, 1500, 1450, 1600, 1550]

# Otra con los días de la semana (7 días)
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Prepara una lista de acumulación:
ventas_acumuladas = [0] * 7  # Inicializa la lista en cero

# Recorre la lista ventas usando un for con enumerate():
for i, venta in enumerate(ventas_por_dia):
    # Esto te permitirá saber en qué posición estás.
    # Usa el índice actual del for para determinar a qué día de la semana corresponde la venta
    dia = i % 7
    ventas_acumuladas[dia] += venta # Suma la venta al día correspondiente, añade cada monto de venta al acumulador del día de la semana correspondiente.

# Imprime el resultado final
for i, total in enumerate(ventas_acumuladas):
    print(f"Total de ventas del {dias_de_la_semana[i]}: {total}")
# Esto mostrará el total de ventas acumuladas por cada día de la semana.

# Mostrar el dia con más ventas
dia_max = ventas_acumuladas.index(max(ventas_acumuladas))
print(f"\nEl día con más ventas fue {dias_de_la_semana[dia_max]} con {ventas_acumuladas[dia_max]} €.")

# Mostrar un media de ventas por día
promedio = sum(ventas_acumuladas) / 7
print(f"\nPromedio de ventas semanales: {promedio:.2f} €")