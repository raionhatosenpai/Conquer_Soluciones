'''Imagina que estás trabajando en el desarrollo de un sistema para una 
aplicación de gestión de documentos en un entorno empresarial. 
Deseas implementar un decorador llamado verificar_acceso_entorno que permita 
controlar el acceso a funciones según el entorno de ejecución.

El decorador debe realizar las siguientes acciones: 

1. Antes de ejecutar la función, verificar si el entorno de ejecución es "producción".

2. Si el entorno es "producción", permitir la ejecución de la función y mostrar 
un mensaje indicando que el acceso fue permitido en el entorno de 
producción.

3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar 
un mensaje indicando que el acceso está restringido a entornos de 
producción.

Luego, aplica este decorador a dos funciones, subir_documento y eliminar_documento.
Intenta ejecutar estas funciones con diferentes entornos y observa el comportamiento del decorador.'''

entorno = "desarrollo" 
# utilizando "desarrollo" como entorno inicial ejecutaremos las funciones en un entorno no permitido.
# si deseas probar el entorno de producción, cambia la variable entorno a "producción" para ver el acceso permitido.

# Decorador para verificar el entorno de ejecución
def verificar_acceso_entorno(funcion):
    def wrapper(*args, **kwargs):
        if entorno == "producción":
            print(f"✅ Acceso permitido en entorno de producción.")
            return funcion(*args, **kwargs)
        else:
            print(f"⛔ Acceso restringido a entornos de producción.")
    return wrapper

# Funciones críticas
@verificar_acceso_entorno
def subir_documento(nombre_documento):
    print(f"📤 Subiendo el documento: '{nombre_documento}' subido exitosamente.")

@verificar_acceso_entorno
def eliminar_documento(nombre_documento):
    print(f"🗑️ Eliminando el documento: '{nombre_documento}' eliminado exitosamente.")

# Menú interactivo
while True:
    print("\n--- Menú de Gestión de Documentos ---")
    print("1. Subir Documento")
    print("2. Eliminar Documento")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del documento a subir: ")
        subir_documento(nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del documento a eliminar: ")
        eliminar_documento(nombre)
    elif opcion == "3":
        print("Saliendo del sistema de gestión de documentos.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
