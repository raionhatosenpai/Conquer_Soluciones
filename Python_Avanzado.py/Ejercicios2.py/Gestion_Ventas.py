# Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
# estructura de datos adecuada para almacenar la información de las ventas
# (por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
# agregar el producto vendido con su precio y otro para mostrar las ventas de
# productos con sus respectivos precios.
#
# (La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: 
# precio1}, {“Producto”: producto2, “Precio”: precio2}…])

ventas = []

def agregar_venta(producto, precio):
    ventas.append({"Producto": producto, "Precio": precio})

def mostrar_ventas():
    for venta in ventas:
        print(f"Producto: {venta['Producto']}, Precio: {venta['Precio']}")
    if not ventas:
        print("No hay ventas registradas.")

# Ejemplos de uso
agregar_venta("Camiseta", 20.0)
agregar_venta("Pantalones", 35.5)
agregar_venta("Zapatos", 50.0)
mostrar_ventas()
print("-" * 30)
agregar_venta("Gorra", 15.0)
mostrar_ventas()
print("-" * 30)
agregar_venta("Chaqueta", 80.0)
mostrar_ventas()
print("-" * 30)
agregar_venta("Calcetines", 5.0)
mostrar_ventas()
print("-" * 30)
agregar_venta("Bufanda", 12.0)
mostrar_ventas()
print("-" * 30)
agregar_venta("Guantes", 8.0)
mostrar_ventas()
print("-" * 30)