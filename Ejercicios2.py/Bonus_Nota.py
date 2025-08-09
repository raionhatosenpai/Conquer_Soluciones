# Bonus beca con nota media 
# nota media minima 8.0
# Edad: 17-21 (Inclusive)

# Solicitar nombre del alumno
nombre = input("Introduce el nombre del alumno: ").title().strip()
# Solicitar nota media del alumno
nota_media = float(input("Introduce la nota media del alumno: "))
# Solicitar edad del alumno
edad = int(input("Introduce la edad del alumno: "))
# Comprobar si el alumno cumple los requisitos para la beca
if nota_media >= 8.0 and 17 <= edad <= 21:
    print(f"\nEl alumno {nombre} es un candidato ideal para la beca, Felicitaciones!.")
else:
    print(f"\nLamentamos comunicar que el alumno {nombre} no cumple los requisitos para la beca.")