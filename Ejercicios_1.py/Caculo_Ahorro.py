# Solicita el nombre del usuario
# Este programa calcula el ahorro anual de una persona
nombre = input("Ingrese su nombre: ")
nombre = nombre.replace(",", " ").replace(".", " ").title()  # Reemplaza comas y puntos por espacios y capitaliza el nombre
print("\nHola, " + nombre + "! Bienvenido al programa de cálculo de ahorro.")

# Solicita los datos al usuario, ingresos por hora y horas trabajadas
ingreso_hora = float(input("\nIntroduce los ingresos por hora: "))
horas_trabajadas = float(input("Introduce las horas trabajadas: "))

# Calcular el salario semanal
salario_semanal = ingreso_hora * horas_trabajadas

# Calcular las ganancias anuales
ganancias_anuales = salario_semanal * 52

# Imprimir por pantalla el resultado
print("\nTu salario anual es: " + str(round(ganancias_anuales, 2)) + " € euros.")

# Calcular gastos semanales
gastos_semanales = float(input("\nIntroduce los gastos semanales: "))

# Calcular gastos anuales
gastos_anuales = gastos_semanales * 52

# Calcular ahorro anual
ahorro_anual = ganancias_anuales - gastos_anuales

# Imprimir por pantalla el resultado
print("\n" + nombre + ", tu ahorro anual es: " + str(round(ahorro_anual, 2)) + " € euros.")

# --- Escenario: Trabajo a tiempo parcial y reducción de gastos ---
horas_parciales = float(input("\nIntroduce las horas trabajadas a tiempo parcial: "))
gastos_parciales = float(input("Introduce tus nuevos gastos semanales reducidos: "))

# Calcular el nuevo salario y gastos anuales
salario_parcial = ingreso_hora * horas_parciales
ganancias_parciales = salario_parcial * 52
gastos_reducidos_anuales = gastos_parciales * 52
ahorro_parcial = ganancias_parciales - gastos_reducidos_anuales

# Imprimir por pantalla el resultado
print("\n" + nombre + ", si trabajas a tiempo parcial y reduces tus gastos, tu ahorro anual sería: " + str(round(ahorro_parcial, 2)) + " € euros.")

# Comprobación: ¿Son suficientes los ingresos parciales para cubrir los gastos reducidos?
if ganancias_parciales >= gastos_reducidos_anuales:
    print("✅ Tus ingresos a tiempo parcial son suficientes para cubrir tus gastos reducidos.")
else:
    print("❌ Tus ingresos a tiempo parcial NO son suficientes para cubrir tus gastos reducidos.")