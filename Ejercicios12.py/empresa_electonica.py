# Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
# analizar los datos de calidad de los componentes utilizados en la producción de dichos
# dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
# producción, el tipo de componente, el lote al que pertenece el componente y la
# puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
# datos para determinar cuál es el tipo de componente con la puntuación de calidad más
# alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
# promedio de cada tipo de componente.

#  puede ser util utilizar np.unique y np.argmax

import numpy as np

# Datos de ejemplo
componentes = np.array([
    ["2023-01-15", "Resistor", "Lote 1", 85],
    ["2023-01-20", "Capacitor", "Lote 2", 90],
    ["2023-02-10", "Resistor", "Lote 3", 80],
    ["2023-02-15", "Capacitor", "Lote 4", 95],
    ["2023-03-05", "Transistor", "Lote 5", 88],
    ["2023-03-12", "Resistor", "Lote 6", 82],
    ["2023-04-20", "Capacitor", "Lote 7", 91],
    ["2023-04-01", "Transistor", "Lote 8", 87],
    ["2023-05-10", "Resistor", "Lote 9", 84],
    ["2023-05-15", "Capacitor", "Lote 10", 92],
    ["2023-06-20", "Transistor", "Lote 11", 89],
    ["2023-06-01", "Resistor", "Lote 12", 86],
    ["2023-07-10", "Capacitor", "Lote 13", 93],
    ["2023-07-15", "Transistor", "Lote 14", 90],
    ["2023-08-01", "Resistor", "Lote 15", 86],
    ["2023-08-10", "Capacitor", "Lote 16", 93],
    ["2023-09-15", "Transistor", "Lote 17", 90],
    ["2023-09-01", "Resistor", "Lote 18", 86],
    ["2023-10-10", "Capacitor", "Lote 19", 93],
    ["2023-10-15", "Transistor", "Lote 20", 90],
    ["2023-11-01", "Resistor", "Lote 21", 86],
    ["2023-11-05", "Capacitor", "Lote 22", 92],
    ["2023-12-10", "Transistor", "Lote 23", 89],
    ["2023-12-01", "Resistor", "Lote 24", 86]
    ])

# cuál es el tipo de componente con la puntuación de calidad más alta
tipos, indices = np.unique(componentes[:, 1], return_inverse=True)
max_indices = np.argmax(componentes[:, 3].astype(int), axis=0)
tipo_max = tipos[indices[max_indices]]
print("Tipo de componente con la puntuación más alta:", tipo_max, "con una puntuación de", componentes[max_indices, 3])

# cuántos componentes se produjeron en cada mes
fechas = np.array([fecha.split("-")[1] for fecha in componentes[:, 0]])
meses, conteos = np.unique(fechas, return_counts=True)
print("Cantidad de componentes producidos por mes:")
for mes, conteo in zip(meses, conteos):
    print(f"Mes {mes}: {conteo} componentes")

    # cuál es la puntuación de calidad promedio de cada tipo de componente
    for tipo in tipos:
        puntuaciones = componentes[componentes[:, 1] == tipo, 3].astype(int)
        if puntuaciones.size > 0:
            print(f"Puntuación promedio de {tipo}: {np.mean(puntuaciones):.2f}")
    print("-----------------------------------------------")       