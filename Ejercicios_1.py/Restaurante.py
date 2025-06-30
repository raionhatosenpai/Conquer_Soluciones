menu = {"Ensalada mixta" : 12, 
         "Sopa de pescado" : 10,
          "Dorada al horno" : 18,
           "Arroz al curry" : 14,
            "Lasaña de carne" : 15,
              "Brownie de chocolate" : 8,
                "Helado" : 6,
                 "Refrescos" : 5.5,
                   "Café" : 3.5 } # (menu = {}) crea un diccionario en el cual esta integrados todos los platos y sus precios

total = 0 #se inicializa la variable total a 0
for plato in menu: # se itera sobre cada plato en el diccionario menu
    cantidad = int(input(f"¿Cuántos '{plato}' se han pedido? ")) # se pide la cantidad de cada plato uno a uno
    if cantidad > 0: #Validad que la cantidad sea mayor que 0
        print(f"Se han servido {cantidad} '{plato}'")
    else:
        print(f"No se han servido '{plato}'")
    
    total += menu[plato] * cantidad  # se multiplica la cantidad de cada plato por su precio y se suma al total
    # menu[plato] accede al precio del plato en el diccionario menu
    # total += menu[plato] * cantidad suma el precio del plato multiplicado por la cantidad al total

print(f"El total de la cuenta es: {total:.2f} €") #se imprime el total de la cuenta .2f indica el total con dos decimales
