# crea un script que cree un grupo de alumnos por nombre, sexo y les asigne una clase Grupo A o Grupo B

sexo = input("Ingrese el sexo del alumno (M/F): ").upper() # M para masculino, F para femenino
nombre = input("Ingrese el nombre del alumno: ").title() # Capitaliza el nombre
# Verifica si el nombre comienza con una letra entre E y M para asignar el grupo y el sexo
if (sexo == 'F'):
    if 'E' <= nombre[0] <= 'M':
        clase = 'Grupo A'
    else:
        clase = 'Grupo B'
elif (sexo == 'M'): # Verifica si el sexo es masculino
    # Verifica si el nombre comienza con una letra entre A y H o entre R y Z para asignar el grupo
    if  ('A' <= nombre[0] <= 'H') or ('R' <= nombre[0] <= 'Z'):
        clase = 'Grupo A'
    else:
        clase = 'Grupo B'
else: # Si el sexo no es reconocido, dara un mensaje de error
    clase = 'Grupo No Asignado'       
    print("Sexo no reconocido. Usa 'M' para masculino o 'F' para femenino.")
# Imprime el resultado final
if clase != 'Grupo No Asignado':
    print(f"El alumno {nombre} de sexo {sexo} pertenece al {clase}.")