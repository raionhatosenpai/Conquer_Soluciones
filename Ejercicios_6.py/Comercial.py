# Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
# la cantidad total de ventas, el dinero facturado por producto y el dinero total.

# lista de productos 
productos = { 1: 30.0, 2: 9.80, 3: 42.5, 4: 32.6, 5: 71.5,
                 6: 44.0, 7: 21.2, 8: 53.2, 9: 25.3, 10: 57.8} 

# solicitar al usuario el número de unidades vendidas de cada producto teniendo en cuenta errores 
unidades_vendidas = {}
for producto in productos:
    while True:
        try:
            unidades = int(input(f"Introduce el número de unidades vendidas del producto {producto}: "))
            if unidades < 0:
                raise ValueError("El número de unidades no puede ser negativo.")
            unidades_vendidas[producto] = unidades
            break
        except ValueError: # manejar errores de entrada
            print(f"Error: Por favor, introduce un número válido.")
print(" ")

# calcular el dinero facturado por producto y el total
total_ventas = 0
for producto, precio in productos.items():
    unidades = unidades_vendidas.get(producto, 0)
    dinero_facturado = precio * unidades
    total_ventas += dinero_facturado
    print(f"Producto {producto}: {unidades} unidades vendidas, Dinero facturado: {dinero_facturado:.2f} €")
print(" ")
    
# imprimir la cantidad total de ventas
print(f"Cantidad total de ventas: {sum(unidades_vendidas.values())} unidades")
print(f"Total ventas: {total_ventas:.2f} €")