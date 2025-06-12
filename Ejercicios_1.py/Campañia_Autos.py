# Precio de cada tipo de vehiculo
precio_serie_1 = 20000    
precio_serie_plus = 35000
precio_todo_terreno = 60000

# La comision de venta por cada tipo de vehiculo
comision_1 = 0.03 
comision_plus = 0.05
comision_terreno = 0.07

# Solicito el Nº de vehiculos vendidos
serie_1_vendidos = int(input("Introduce el Nº de vehiculos vendidos de la RBM serie 1: "))  
serie_plus_vendidos = int(input("Introduce el Nº de vehiculos vendidos de la RBM serie plus: "))
todo_terreno_vendidos = int(input("Introduce el Nº de vehiculos vendidos de RBM todo terreno: "))

# Calculo la comision de cada tipo de vehiculo vendido
total_serie_1 = serie_1_vendidos * precio_serie_1 * comision_1
total_serie_plus = serie_plus_vendidos * precio_serie_plus * comision_plus
total_todo_terreno = todo_terreno_vendidos * precio_todo_terreno * comision_terreno

# Calculo el total de la comision de venta
total_comision = total_serie_1 + total_serie_plus + total_todo_terreno

# Mostrar el resultado
print("\nResumen de comisiones:")
print(f"Comisión por RBM Serie 1: {round(total_serie_1, 2)} €") 
print(f"Comisión por RBM Serie Plus: {round(total_serie_plus, 2)} €")
print(f"Comisión por RBM Todoterreno: {round(total_todo_terreno, 2)} €")
print(f"Comisión total del mes: {round(total_comision, 2)} €")
 #\n es un salto de línea, crea un espacio entre la línea anterior (25) y la siguiente (26).
 # f{} es un formato de cadena Las f-strings permiten incluir expresiones dentro de una cadena utilizando llaves {}.
 # Estas expresiones se evalúan y se reemplazan por su valor correspondiente.