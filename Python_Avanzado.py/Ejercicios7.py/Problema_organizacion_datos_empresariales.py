# Tu tarea es organizar una lista consolidada de todos los empleados de la 
# empresa. 
# La organización debe seguir ciertas reglas:

# - Los empleados se deben ordenar por el rendimiento en proyectos recientes 
# de forma descendente.

# - Para aquellos con el mismo rendimiento, se deben ordenar por edad de 
# forma ascendente.
# 
# - Agrupar a los empleados por país para 
# un análisis más efectivo. 
# 
# Utiliza funciones lamba.

from itertools import groupby

def ordenar_empleados(empleados):
    # Ordenar por rendimiento (descendente) y luego por edad (ascendente)
    empleados_ordenados = sorted(empleados, key=lambda emp: (emp['pais'], -emp['rendimiento'], emp['edad']))
    return empleados_ordenados

# Agrupar por país
def agrupar_por_pais(empleados_ordenados):
        empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados, key=lambda emp: emp['pais'])}
        return empleados_agrupados

# Devolver empleados agrupados por país
def mostrar_empleados(empleados_agrupados):
     for pais, grupo_empleados in empleados_agrupados.items():
        print(f"\nPaís: {pais}")
        for empleado in grupo_empleados:
          print(empleado)

# Datos de ejemplo
empleados = [
    {'nombre': 'Ana', 'edad': 30, 'pais': 'España', 'rendimiento': 85},
    {'nombre': 'Juan', 'edad': 24, 'pais': 'Argentina', 'rendimiento': 80},
    {'nombre': 'Luis', 'edad': 25, 'pais': 'México', 'rendimiento': 90},
    {'nombre': 'Carlos', 'edad': 28, 'pais': 'España', 'rendimiento': 85},
    {'nombre': 'Marta', 'edad': 35, 'pais': 'México', 'rendimiento': 95},
    {'nombre': 'Sofía', 'edad': 22, 'pais': 'Argentina', 'rendimiento': 90},
    {'nombre': 'Lucía', 'edad': 29, 'pais': 'España', 'rendimiento': 80},
    {'nombre': 'Diego', 'edad': 31, 'pais': 'México', 'rendimiento': 85},]

empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_por_pais(empleados_ordenados)
mostrar_empleados(empleados_agrupados)