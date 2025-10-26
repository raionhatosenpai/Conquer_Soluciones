#  Imagina que estás desarrollando un sistema complejo que incluye múltiples 
# funciones críticas. Para asegurarte de que todo funcione correctamente y para 
# realizar un seguimiento del tiempo de ejecución de estas funciones, decides 
# implementar un decorador de registro (logger) con tiempo de ejecución.
# El decorador debería realizar las siguientes acciones:

# 1. Antes de llamar a la función original (puedes incluir cualquier función), 
# debe imprimir un mensaje indicando que la función está a punto de 
# ejecutarse.

# 2. Después de que la función se haya ejecutado, debe imprimir un mensaje 
# que incluya el tiempo que tardó la función en ejecutarse

# 3.  Si la función original arroja una excepción, el decorador debe manejarla e 
# imprimir un mensaje adecuado, indicando que se ha producido una 
# excepción.

import time

# Decorador de logger con tiempo de ejecución
def logger_con_tiempo(funcion):
    def wrapper(*args, **kwargs):# acepta cualquier numero de argumentos
        print(f"Ejecutando la función '{funcion.__name__}'...")
        inicio_tiempo = time.time()
        try:# intentar ejecutar la funcion
            resultado = funcion(*args, **kwargs)
            fin_tiempo = time.time()
            tiempo_ejecucion = fin_tiempo - inicio_tiempo
            print(f"La función '{funcion.__name__}' se ejecutó en {tiempo_ejecucion:.4f} segundos.")
            return resultado
        except Exception as e:# manejar excepcion
            print(f"Se produjo una excepción en la función '{funcion.__name__}': {e}")
    return wrapper

# Ejemplo de uso del decorador
@logger_con_tiempo
def funcion_ejemplo(x):
    """Función de ejemplo que simula un trabajo con una pausa."""
    time.sleep(x)
    return x * 2
# Llamada a la función decorada
resultado = funcion_ejemplo(2)
print(f"Resultado de la función: {resultado}")
print()

# Ejemplo de uso del decorador con una función que lanza una excepción
@logger_con_tiempo
def funcion_con_error():
    """Función de ejemplo que lanza una excepción."""
    raise ValueError("Este es un error intencional.")
# Llamada a la función decorada que lanza una excepción
funcion_con_error()
print()

# funcion con secuencia de Fibonacci
@logger_con_tiempo
def fibonacci(n):
    if n <= 0:
        raise ValueError("El número debe ser mayor que 0.")
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

# Uso de ejemplo
fibonacci(10000)