euros = input("Introduce la cantidad de euros a cambiar: ")

dolares_bruto = float(euros) * 1.2 # realiza la conversion de euros a dolares

porc_cambio = 0.10 # porcentaje de cambio

comision = float(dolares_bruto) * porc_cambio # comision de la casa de cambios

dolares_neto = float(dolares_bruto) - float(comision) # dolares netos

dolares = round(dolares_neto, 2) # redondea a 2 decimales

# el resultado final
print("Has introducido:      {", euros ,"} Euros €")
print("Tipo de cambio:       {1.2} $ Dollar por Euros €")
print("Dólares (brutos):     {", round(dolares_bruto, 2) ,"} Dollar $")
print("Comisión (10%):       {", round(comision, 2) ,"} Dollar $") # Opinion personal: --- ! ESTO ES UN ATRACO ! ---
print("Dólares a recibir:    {", round(dolares_neto, 2) ,"} Dollar $")
