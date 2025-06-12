# Pedir al usuario su nombre y mostrar un mensaje de bienvenida
nombre = input("¿Cual es tu nombre? ")

# De esta forma el programa imprime el input de manera correcta
Mensaje = ('!Hola '+ nombre.replace(","," ").replace("."," ").title() +' estas usando Python!') 

#.upper()/.lower()para que todo el mensaje este en mayusculas o minusculas)
print(Mensaje)