# Supongamos que tienes un conjunto de datos de películas que contiene información
# sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
# estos datos para determinar cuál es el género de película más popular, cuántas películas
# se lanzaron en cada década y cuál es la duración promedio de cada género de película.
# puede ser util utilizar np.unique, np.argsort y np.count_nonzero

import numpy as np

# Datos de ejemplo
peliculas = np.array([
    ["Película A", "Acción", 120, 2001, 7.5],
    ["Película B", "Comedia", 90, 2005, 6.0],
    ["Película C", "Acción", 150, 2010, 8.0],
    ["Película D", "Drama", 130, 2000, 9.0],
    ["Película E", "Comedia", 100, 2015, 7.0],
    ["Película F", "Acción", 140, 2020, 8.5],
    ["Película G", "Drama", 110, 2018, 7.5],
    ["Película H", "Comedia", 95, 2021, 6.5],
    ["Película I", "Acción", 125, 2022, 8.0],
    ["Película J", "Drama", 115, 2023, 7.0]
])

# analizar estos datos para determinar cuál es el género de película más popular, utilizando np.unique, np.argsort y np.count_nonzero
generos, conteos_generos = np.unique(peliculas[:, 1], return_counts=True)
conteos_generos_invertidos = np.argsort(conteos_generos)[::-1][0]# toma el indice mas alto
print("\nGénero de película más popular:", generos[conteos_generos_invertidos])

# cuántas películas se lanzaron en cada década, utilizando np.unique, np.argsort y np.count_nonzero
decadas = np.unique(peliculas[:, 3].astype(int) // 10 * 10, return_counts=True)

# Conteo de películas por década
conteos_decadas = []
for decada in decadas[0]:
    conteo = np.count_nonzero((peliculas[:, 3].astype(int) >= decada) & (peliculas[:, 3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)
    print("\nPelículas lanzadas en cada década:", decada, " se crearon:", conteos_decadas[-1], " peliculas")

# Duración promedio de cada género de película
duracion_promedio = []
duraciones = peliculas[:, 2]
duracion_media = np.zeros(len(generos))
for i in range(len(generos)):
    duracion_media[i] = np.mean(duraciones[peliculas[:, 1] == generos[i]].astype(float))
    print("\nDuración promedio del género", generos[i], ":", duracion_media[i].round(2))