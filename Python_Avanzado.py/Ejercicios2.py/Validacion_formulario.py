# Crea un programa que valide un formulario de registro. Crea una función
# llamada validar_formulario que reciba diferentes campos de un formulario
# (nombre, correo electrónico y número de teléfono) y verifique si los valores
# ingresados cumplen con los requisitos especificados, siendo estos:
#
# 1. Que el nombre tenga una longitud minima de 3 caracteres
# 2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 caracteres
# 3. Que el email contenga un “@“ y un “.”

def validar_formulario(Nombre, Email, Telefono):
    if len(Nombre) < 3:
        return "El nombre debe tener al menos 3 caracteres."
    if not Telefono.isdigit() or len(Telefono) != 9:
        return "El teléfono debe tener 9 dígitos."
    if "@" not in Email or "." not in Email:
        return "El email debe contener un '@' y un '.'."
    return "Formulario válido."

# Ejemplos de uso
Nombre = input("Introduce tu nombre: ")
Email = input("Introduce tu email: ")
Telefono = input("Introduce tu teléfono: ")
print(validar_formulario(Nombre, Email, Telefono))

# print(validar_formulario("Ana", "ana@example.com", "123456789"))
# print(validar_formulario("Jose", "jose@examplecom", "12345689"))
# print(validar_formulario("Luis", "luis@example.com", "123456789"))
# print(validar_formulario("Al", "al@example.com", "123456789"))
# print(validar_formulario("Maria", "maria@example.com", "123456789"))
# print(validar_formulario("Marta", "marta@examplecom", "123456789"))