# Crea una clase "Producto" con atributos como nombre, precio y cantidad en 
# stock. Luego, crea una clase "Tienda" que contenga una lista de productos 
# disponibles y métodos para agregar productos, mostrar el inventario y 
# realizar una compra.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} €, Cantidad en stock: {self.cantidad}"
    
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en la tienda.")
            return
        print("Inventario de la tienda:")
        for producto in self.productos:
            print(producto)

    def realizar_compra(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad:
                    total = producto.precio * cantidad
                    producto.cantidad -= cantidad
                    print(f"Compra exitosa: {cantidad} x {producto.nombre}. Total a pagar: {total} €.")
                    return
                else:
                    print(f"No hay suficiente stock de '{nombre_producto}'. Stock disponible: {producto.cantidad}")
                    return
        print(f"Producto '{nombre_producto}' no encontrado en la tienda.")

# Ejemplo de uso
tienda = Tienda()
while True:
    accion = input("¿Desea agregar producto (a), mostrar inventario (m), realizar compra (c) o salir (q)? ").lower()
    if accion == 'a':
        nombre = input("Ingrese el nombre del producto: ").upper()
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock: "))
            producto = Producto(nombre, precio, cantidad)
            tienda.agregar_producto(producto)
        except ValueError:
            print("Por favor, ingrese un precio y cantidad válidos.")
    elif accion == 'm':
        tienda.mostrar_inventario()
    elif accion == 'c':
        nombre_producto = input("Ingrese el nombre del producto a comprar: ").upper()
        try:
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            tienda.realizar_compra(nombre_producto, cantidad)
        except ValueError:
            print("Por favor, ingrese una cantidad válida.")
    elif accion == 'q':
        print("Saliendo del programa.")
        exit()  # Sale del programa
    else:
        print("Acción no reconocida. Por favor, ingrese 'a', 'm', 'c' o 'q'.")