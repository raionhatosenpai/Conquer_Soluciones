# Entrada de texto con los datos de varios alumnos
datos = '''David Fernandez 12311267A 43527 1 9.1 7.6 2.4
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4
Juan Perez 647829236A 43527 3 8.1 8.5 8.4'''

# Lista para guardar la información de todos los alumnos
alumnos = []

# Procesar línea por línea
for linea in datos.strip().split('\n'):
    partes = linea.strip().split()
    nombre = partes[0]
    apellido = partes[1]
    dni = partes[2]
    cod_asignatura = partes[3]
    convocatoria = partes[4]
    notas = list(map(float, partes[5:]))  # Convertir notas a float
    alumno = [nombre, apellido, dni, cod_asignatura, convocatoria] + notas
    alumnos.append(alumno)

# Calcular la nota media y mostrar el DNI
for alumno in alumnos:
    dni = alumno[2]
    notas = alumno[5:]
    media = sum(notas) / len(notas)
    print(f"Nombre y Apellidos: {alumno[0]} {alumno[1]}, DNI: {dni}, Nota media: {media:.2f}, Convocatoria: {alumno[4]}")
