# Crea una clase llamada "Calculadora" con métodos para sumar, restar, 
# multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones 
# básicas.

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Dvisión por cero no permitida."
        
# Solicitar al usuario que ingrese dos números y la operación a realizar
def main():
    while True:
      calc = Calculadora()
    
      print("\nOperaciones disponibles: 1 = (sumar), 2 = (restar), 3 = (multiplicar), 4 = (dividir), 5 = (salir)")
      operacion = input("Ingrese la operación que desea realizar: ").strip().lower()

      if operacion == "5":
            print("Saliendo del programa.")
            break

      try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
      except ValueError:
        print("Error: Por favor ingrese números válidos.")
        continue
    
      if operacion == "1":
        resultado = calc.sumar(num1, num2)
      elif operacion == "2":
        resultado = calc.restar(num1, num2)
      elif operacion == "3":
        resultado = calc.multiplicar(num1, num2)
      elif operacion == "4":
        resultado = calc.dividir(num1, num2)
      else:
        print("Operación no válida.")
        continue
     
      print(f"El resultado de {operacion} {num1} y {num2} es: {resultado}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main() 