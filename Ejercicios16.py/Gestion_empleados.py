# Imagina que eres el gerente de recursos humanos de una empresa y
# necesitas gestionar la información de los empleados. Cada empleado
# tiene un nombre, salario y departamento al que pertenece. Implementa
# un programa en Python que permita agregar nuevos empleados,
# actualizar el salario de un empleado existente, mostrar la lista completa
# de empleados y calcular el promedio salarial por departamento.

empleados = {}

# Función para agregar un nuevo empleado
def agregar_empleado(nombre, salario, departamento):
    empleados[nombre] = {
        "salario": salario,
        "departamento": departamento
    }

# Función para actualizar el salario de un empleado existente
def actualizar_salario(nombre, nuevo_salario):
    if nombre in empleados:
        empleados[nombre]["salario"] = nuevo_salario
    else:
        print("El empleado no existe.")

# Función para mostrar la lista completa de empleados
def mostrar_empleados():
    for nombre, info in empleados.items():
        print(f"Empleado: {nombre}")
        print(f"  Salario: {info['salario']}")
        print(f"  Departamento: {info['departamento']}")

# Función para calcular el promedio salarial por departamento
def calcular_promedio_departamento(departamento):
    salarios = [info["salario"] for info in empleados.values() if info["departamento"] == departamento]
    if salarios:
        promedio = sum(salarios) / len(salarios)
        print(f"El promedio salarial en el departamento {departamento} es: {promedio}")
    else:
        print(f"No hay empleados en el departamento {departamento}.")

# Bucle principal del programa
while True:
    print("\nOpciones:")
    print("1. Agregar empleado")
    print("2. Actualizar salario")
    print("3. Mostrar empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        nombre = input("Nombre del empleado: ").title()
        salario = float(input("Salario del empleado: "))
        departamento = input("Departamento del empleado: ")
        agregar_empleado(nombre, salario, departamento)
    elif opcion == "2":
        nombre = input("Nombre del empleado a actualizar: ").title()
        nuevo_salario = float(input("Nuevo salario: "))
        actualizar_salario(nombre, nuevo_salario)
    elif opcion == "3":
        mostrar_empleados()
    elif opcion == "4":
        departamento = input("Departamento para calcular el promedio salarial: ")
        calcular_promedio_departamento(departamento)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")