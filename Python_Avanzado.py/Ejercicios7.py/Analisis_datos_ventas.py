# Cada venta se representa 
# como un diccionario, que incluye el nombre del producto, la fecha de venta, el 
# monto de la venta y la ubicación del comprador. Realiza un análisis avanzado 
# de estas ventas.

# 1. Filtra las ventas realizadas en el último trimestre del año.
# 2. Selecciona solo las ventas de productos con un monto superior a $500.
# 3. Agrupa las ventas por ubicación del comprador.
# 4. Calcula el promedio del monto de venta para cada ubicación.
# 5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente.
# Utiliza funciones lambda.

from datetime import datetime

def analizar_ventas(ventas):
    # 1. Filtrar ventas del último trimestre del año
    ventas_ultimo_trimestre = list(filter(
        lambda venta: datetime.strptime(venta['fecha_venta'], '%Y-%m-%d').month in [10, 11, 12],
        ventas
    ))

    # 2. Seleccionar ventas con monto superior a $500
    ventas_monto_alto = list(filter(
        lambda venta: venta['monto_venta'] > 500,
        ventas_ultimo_trimestre
    ))

    # 3. Agrupar ventas por ubicación del comprador
    ventas_por_ubicacion = {}
    for venta in ventas_monto_alto:
        ubicacion = venta['ubicacion_comprador']
        if ubicacion not in ventas_por_ubicacion:
            ventas_por_ubicacion[ubicacion] = []
        ventas_por_ubicacion[ubicacion].append(venta['monto_venta'])

    # 4. Calcular el promedio del monto de venta para cada ubicación
    promedios_por_ubicacion = {}
    for ubicacion, montos in ventas_por_ubicacion.items():
        promedio = sum(montos) / len(montos)
        promedios_por_ubicacion[ubicacion] = promedio

    # 5. Ordenar las ubicaciones por el promedio del monto de venta de forma descendente
    ubicaciones_ordenadas = sorted(
        promedios_por_ubicacion.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return ubicaciones_ordenadas
# Ejemplo de uso
ventas = [
    {'producto': 'Laptop', 'fecha_venta': '2023-10-15', 'monto_venta': 1200, 'ubicacion_comprador': 'Ciudad A'},
    {'producto': 'Desktop', 'fecha_venta': '2023-08-22', 'monto_venta': 750, 'ubicacion_comprador': 'Ciudad B'},
    {'producto': 'Printer', 'fecha_venta': '2023-11-10', 'monto_venta': 550, 'ubicacion_comprador': 'Ciudad C'},
    {'producto': 'Router', 'fecha_venta': '2023-12-05', 'monto_venta': 600, 'ubicacion_comprador': 'Ciudad A'},
    {'producto': 'Scanner', 'fecha_venta': '2023-10-25', 'monto_venta': 650, 'ubicacion_comprador': 'Ciudad B'},
    {'producto': 'Smartphone', 'fecha_venta': '2023-11-20', 'monto_venta': 800, 'ubicacion_comprador': 'Ciudad B'},
    {'producto': 'Tablet', 'fecha_venta': '2023-09-05', 'monto_venta': 500, 'ubicacion_comprador': 'Ciudad A'},
    {'producto': 'Monitor', 'fecha_venta': '2023-12-01', 'monto_venta': 600, 'ubicacion_comprador': 'Ciudad C'},
    {'producto': 'Headphones', 'fecha_venta': '2023-10-30', 'monto_venta': 1050, 'ubicacion_comprador': 'Ciudad B'},
    {'producto': 'Camera', 'fecha_venta': '2023-11-15', 'monto_venta': 700, 'ubicacion_comprador': 'Ciudad A'},
    {'producto': 'Speakers', 'fecha_venta': '2023-12-10', 'monto_venta': 450, 'ubicacion_comprador': 'Ciudad C'},
    {'producto': 'External Hard Drive', 'fecha_venta': '2023-10-18', 'monto_venta': 520, 'ubicacion_comprador': 'Ciudad A'},
    {'producto': 'Webcam', 'fecha_venta': '2023-11-22', 'monto_venta': 480, 'ubicacion_comprador': 'Ciudad B'},
    {'producto': 'Microphone', 'fecha_venta': '2023-12-15', 'monto_venta': 610, 'ubicacion_comprador': 'Ciudad C'},
]

resultado = analizar_ventas(ventas)
print("Ubicación     | Promedio de Venta")
print("-------------------------------")
for ubicacion, promedio in resultado:
    print(f"{ubicacion:<13} | ${promedio:.2f}")
