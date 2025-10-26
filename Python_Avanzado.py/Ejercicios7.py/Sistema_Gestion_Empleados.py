#  Crea un sistema de clases que maneje la información de 
#  los empleados, incluyendo empleados a tiempo completo y empleados a 
#  tiempo parcial.

# - Clase base: `Empleado`
# - Atributos: nombre, apellido, salario base

# - Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
# - Atributo adicional: bono anual

# - Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
# - Atributo adicional: horas trabajadas por semana

# Resuelve el problema creando instancias de estas clases y calculando los 
# salarios totales para diferentes tipos de empleados

class Empleado:
    # Atributos: nombre, apellido, salario base
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

class EmpleadoTiempoCompleto(Empleado):
    # Atributo adicional: bono anual
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    # Método para calcular el salario total anual
    def calcular_salario_total(self):
        return (self.salario_base * 12) + self.bono_anual
    
class EmpleadoTiempoParcial(Empleado):
    # Atributo adicional: horas trabajadas por semana
    def __init__(self, nombre, apellido, salario_base, horas_trabajadas_semana):
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas_semana = horas_trabajadas_semana

    # Método para calcular el salario total anual
    def calcular_salario_total(self):
        return self.salario_base * self.horas_trabajadas_semana * 52  # 52 semanas en un año

class SistemaGestionEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_salarios(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return  # Salimos antes del bucle
        for empleado in self.empleados:
             salario_total = empleado.calcular_salario_total()
             if isinstance(empleado, EmpleadoTiempoCompleto):
                tipo = "Tiempo Completo"
             else:
                tipo = "Tiempo Parcial"
             print(f"{tipo} | Empleado: {empleado.nombre} {empleado.apellido}, Salario Total Anual: ${salario_total:.2f}")  

# ----- EJEMPLO DE USO -----
# con -menu- interactivo
sistema = SistemaGestionEmpleados()
while True:
    accion = input("¿Desea agregar un empleado (a) o mostrar salarios (m) o salir (s)? ").lower()
    if accion == 's':
        break
    elif accion == 'm':
       sistema.mostrar_salarios()

    if accion == 'a':
        tipo = input("¿Empleado a tiempo completo (c) o tiempo parcial (p)? ").lower()
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        salario_base = float(input("Salario base: "))
        if tipo == 'c':
            bono_anual = float(input("Bono anual: "))
            empleado = EmpleadoTiempoCompleto(nombre, apellido, salario_base, bono_anual)
        elif tipo == 'p':
            horas_trabajadas_semana = float(input("Horas trabajadas por semana: "))
            empleado = EmpleadoTiempoParcial(nombre, apellido, salario_base, horas_trabajadas_semana)
        else:
            print("Tipo de empleado no válido.")
            continue
        sistema.agregar_empleado(empleado)

# Podria crae un método para eliminar empleados, buscar empleados, etc. incluso guardar en un archivo.
# ademas de validar entradas y manejar errores.
# e incluso un método para mostar todos los empleados registrados. y que todo ello se guarde en una .JSON