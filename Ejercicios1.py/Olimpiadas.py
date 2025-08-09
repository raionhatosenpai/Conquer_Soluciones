# Tiempor para cada corredor
# 1º corredor
min_hannah = int(input("Minutos de Hannah Neise: "))
seg_hannah = int(input("Segundos de Hannah Neise: "))
cen_hannah = int(input("Centésimas de Hannah Neise: "))

# 2º corredor
min_narracott = int(input("Minutos de Jackie Narracott: "))
seg_narracott = int(input("Segundos de Jackie Narracott: "))
cen_narracott = int(input("Centésimas de Jackie Narracott: "))

# 3º corredor
min_bos = int(input("Minutos de Kimberley Bos: "))
seg_bos = int(input("Segundos de Kimberley Bos: "))
cen_bos = int(input("Centésimas de Kimberley Bos: "))

# Ahora calculo los tiempos en segundos
tiempo_hannah = (min_hannah * 60) + seg_hannah + (cen_hannah / 100)
tiempo_narracott = (min_narracott * 60) + seg_narracott + (cen_narracott / 100)
tiempo_bos = (min_bos * 60) + seg_bos + (cen_bos / 100)

# Ahora comparo las velocidades
velocidad_hannah = 100 / tiempo_hannah
velocidad_narracott = 100 / tiempo_narracott
velocidad_bos = 100 / tiempo_bos

# Ahora doy los resultados
print("El tiempo de Hannah Neise es: ", round(tiempo_hannah, 2), " segundos y su velocidad es: ", round(velocidad_hannah, 2), " m/s")
print("El tiempo de Jackie Narracott es: ", round(tiempo_narracott, 2), " segundos y su velocidad es: ", round(velocidad_narracott, 2), " m/s")
print("El tiempo de Kimberley Bos es: ", round(tiempo_bos, 2), " segundos y su velocidad es: ", round(velocidad_bos, 2), " m/s")