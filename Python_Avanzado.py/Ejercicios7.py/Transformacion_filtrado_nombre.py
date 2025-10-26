# Imagina que te encuentras desarrollando una herramienta de procesamiento de 
# nombres para una aplicación de gestión de contactos. Tienes una lista de 
# nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:

# 1.  Utiliza la función lambda para transformar una lista de nombres completos 
# al nuevo formato.

# 2.   Filtra la lista para incluir solo los nombres que contienen 
# al menos dos vocales y tienen una longitud mayor a 10 caracteres.

def transformar_y_filtrar_nombres(nombres):
    # 1. Transformar nombres al formato "Nombre Apellido"
    nombres_transformados = list(map(
        lambda nombre: ' '.join(reversed(nombre.replace(',', ', ').split(', '))),
        nombres))

    # 2. Filtrar nombres con al menos dos vocales y longitud mayor a 10
    def tiene_dos_vocales_y_longitud(nombre):
        vocales = 'aeiouAEIOU'
        conteo_vocales = sum(1 for char in nombre if char in vocales)
        return conteo_vocales >= 2 and len(nombre) > 10

    nombres_filtrados = list(filter(
        tiene_dos_vocales_y_longitud,
        nombres_transformados
    ))

    return nombres_filtrados

# Ejemplo de uso
nombres = []
while True:
    print("elija una opcion:")
    print("1. agregar nombres y procesar")
    print("2. mostrar resultado procesado")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == '1':
        ingreso = input("Ingrese nombres en formato 'Apellido, Nombre' separados por punto y coma: ")
        nombres += [nombre.strip() for nombre in ingreso.split(';')]
    elif opcion == '2':
         for nombre in nombres:
            print(nombre.title())
         resultado = transformar_y_filtrar_nombres(nombres)
         print(f"\nNombres transformados y filtrados:") 
         for nombre in resultado:
                print(nombre.title())
                print()       
    elif opcion == '3':
        break