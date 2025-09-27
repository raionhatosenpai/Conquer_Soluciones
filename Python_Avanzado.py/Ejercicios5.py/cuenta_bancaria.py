# Crea una clase "CuentaBancaria" con atributos como número de cuenta y 
# saldo. Implementa métodos para depositar y retirar dinero, y muestra el 
# saldo actual

# creación de la clase CuentaBancaria junto con sus métodos
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0):# Saldo inicial por defecto es 0
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:# Solo se permiten depósitos positivos
            self.saldo += cantidad
            print(f"Depósito exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")
    def retirar(self, cantidad):# Solo se permiten retiros si hay fondos suficientes
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")
    def mostrar_saldo(self):# Muestra el saldo actual
        print(f"Saldo actual: {self.saldo}")

# Ejemplo de uso
while True:
    numero_cuenta = input("Ingrese el número de cuenta: ")# Solicita el número de cuenta al usuario
    cuenta = CuentaBancaria(numero_cuenta)

    while True:# Bucle para permitir múltiples operaciones
        accion = input("¿Desea depositar (d), retirar (r) o mostrar saldo (s)? (q para salir): ").lower()
        if accion == 'd':# Depósito de dinero
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")
        elif accion == 'r':# Retiro de dinero
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")
        elif accion == 's':# Mostrar saldo
            cuenta.mostrar_saldo()
        elif accion == 'q':# Salir del programa
            print("Saliendo del programa.")
            exit() # Sale del programa se puede variar por un -break- si se desea continuar con otra cuenta
        else:
            print("Acción no reconocida. Por favor, ingrese 'd', 'r', 's' o 'q'.")