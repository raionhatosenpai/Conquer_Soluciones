# Crea un sistema de gestión de una biblioteca utilizando clases en Python. 
# Debes implementar las siguientes clases:
# 1. “Libro”: Representa un libro con atributos como título, autor y número de ejemplares disponibles.
# 2. “Usuario”: Representa a un usuario de la biblioteca con atributos como 
# nombre, número de identificación y lista de libros prestados.
# 3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
# libros, prestar libros a usuarios, devolver libros y mostrar el inventario

# importar json para guardar los datos en un archivo .json
import json

# 1° crear la clase libro con sus atributos
class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ejemplares disponibles: {self.ejemplares}'
    
# 2° crear la clase usuario con sus atributos
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = [] # Lista de libros prestados al usuario

    def __str__(self):
        return f'Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}'
    
# 3° crear la clase biblioteca con sus atributos y métodos
class Biblioteca:
    def __init__(self):
        self.libros = [] # Lista de libros en la biblioteca
        self.usuarios = [] # Lista de usuarios registrados en la biblioteca

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Libro "{libro.titulo}" agregado a la biblioteca.')

    # Método para registrar un usuario en la biblioteca
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'Usuario "{usuario.nombre}" registrado en la biblioteca.')

    # Método para prestar un libro a un usuario 
    def prestar_libro(self, titulo_libro, id_usuario):
        libro = next((libro for libro in self.libros if libro.titulo == titulo_libro), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
        
        if libro and usuario:
            if libro.ejemplares > 0:
                libro.ejemplares -= 1
                usuario.libros_prestados.append(libro)
                print(f'Libro "{libro.titulo}" prestado a usuario "{usuario.nombre}".')
            else:
                print(f'No hay ejemplares disponibles del libro "{libro.titulo}".')
        else:
            if not libro:
                print(f'El libro "{titulo_libro}" no está en la biblioteca.')
            if not usuario:
                print(f'El usuario con ID "{id_usuario}" no está registrado en la biblioteca.')

    # Método para devolver un libro a la biblioteca
    def devolver_libro(self, titulo_libro, id_usuario):
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
        
        if usuario:
            libro = next((libro for libro in usuario.libros_prestados if libro.titulo == titulo_libro), None)
            if libro:
                libro.ejemplares += 1
                usuario.libros_prestados.remove(libro)
                print(f'Libro "{libro.titulo}" devuelto por usuario "{usuario.nombre}".')
            else:
                print(f'El usuario "{usuario.nombre}" no tiene prestado el libro "{titulo_libro}".')
        else:
            print(f'El usuario con ID "{id_usuario}" no está registrado en la biblioteca.')

    # Método para mostrar el inventario de la biblioteca
    def mostrar_inventario(self):
        if self.libros:
            print('Inventario de la biblioteca:')
            for libro in self.libros:
                print(libro)
        else:
            print('La biblioteca no tiene libros en su inventario.')

# Guardar y cargar datos de la biblioteca en un archivo JSON   
    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as file:
                datos = json.load(file)
                for libro_data in datos.get('libros', []):
                    libro = Libro(libro_data['titulo'], libro_data['autor'], libro_data['ejemplares'])
                    self.libros.append(libro)
                for usuario_data in datos.get('usuarios', []):
                    usuario = Usuario(usuario_data['nombre'], usuario_data['id_usuario'])
                    for titulo_libro in usuario_data.get('libros_prestados', []):
                        libro = next((libro for libro in self.libros if libro.titulo == titulo_libro), None)
                        if libro:
                            usuario.libros_prestados.append(libro)
                    self.usuarios.append(usuario)
            print(f'Datos de la biblioteca cargados desde "{archivo}".')
        except FileNotFoundError:
            None
        except json.JSONDecodeError:
            print(f'El archivo "{archivo}" está corrupto o vacío. Iniciando con una biblioteca vacía.')

# Método para guardar datos de la biblioteca en un archivo JSON
    def guardar_datos(self, archivo):
        datos = {
            'libros': [{'titulo': libro.titulo, 'autor': libro.autor, 'ejemplares': libro.ejemplares} for libro in self.libros],
            'usuarios': [{'nombre': usuario.nombre, 'id_usuario': usuario.id_usuario, 'libros_prestados': [libro.titulo for libro in usuario.libros_prestados]} for usuario in self.usuarios]
        }
        with open(archivo, 'w') as file:
            json.dump(datos, file)
        print(f'Datos de la biblioteca guardados en "{archivo}".')

# Ejemplo de uso del sistema de gestión de biblioteca, en base a un menú simple Ejem.
# (1. Agregar libro, 2. Registrar usuario, 3. Prestar libro, 4. Devolver libro, 5. Mostrar inventario, 6. Salir)

# Crear una instancia de la biblioteca y cargar datos desde un archivo
biblioteca = Biblioteca()
archivo_datos = "biblioteca.json"
biblioteca.cargar_datos(archivo_datos)

# Bucle para interactuar con el usuario mediante un menú simple
while True:
    accion = input("¿Desea agregar libro (1), registrar usuario (2), prestar libro (3), devolver libro (4), mostrar inventario (5) o salir (6)? ")
    # Si la acción es '6', salir del bucle y terminar el programa

    # Si la acción es '1', realizar el proceso de agregar un libro
    if accion == '1':
        # solicitar título y autor del libro
        titulo = input("Ingrese el título del libro: ").title() # .title() para que la primera letra de cada palabra sea mayúscula
        autor = input("Ingrese el autor del libro: ").title()
        try:
            # solicitar número de ejemplares y manejar el error si no es un número válido
            ejemplares = int(input("Ingrese el número de ejemplares disponibles: "))
            libro = Libro(titulo, autor, ejemplares)
            biblioteca.agregar_libro(libro)
        # manejar el error si el usuario ingresa un valor no numérico para los ejemplares
        except ValueError:
            print("Por favor, ingrese un número válido para los ejemplares.")
    # Si la acción es '2', realizar el proceso de registrar un usuario            
    elif accion == '2':
        nombre = input("Ingrese el nombre del usuario: ").title()
        try:
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
        except ValueError:
            print("Por favor, ingrese un ID válido para el usuario (-solo admite valor nùmerico-).")
    
    # Si la acción es '3', realizar el proceso de prestar un libro
    elif accion == '3':
        titulo_libro = input("Ingrese el título del libro a prestar: ").title()
        id_usuario = input("Ingrese el ID del usuario: ")
        biblioteca.prestar_libro(titulo_libro, id_usuario)
    
    # Si la acción es '4', realizar el proceso de devolver un libro
    elif accion == '4':
        titulo_libro = input("Ingrese el título del libro a devolver: ").title()
        id_usuario = input("Ingrese el ID del usuario: ")
        biblioteca.devolver_libro(titulo_libro, id_usuario)
    
    # Si la acción es '5', mostrar el inventario de la biblioteca
    elif accion == '5':
        biblioteca.mostrar_inventario()

    # Si la acción es '6', salir del programa
    elif accion == '6':
        biblioteca.guardar_datos(archivo_datos)
        print("Datos guardados correctamente. Saliendo del programa.")
        break # Sale del bucle y termina el programa
    else:
        print("Acción no reconocida. Por favor, elija una acción valida.")

# Al finalizar el programa, guardar los datos de la biblioteca en el archivo JSON
# se puede implementar en el menú, opción mostrar usuario para ver los id y nombres de los usuarios registrados
# y así facilitar la tarea de prestar y devolver libros a los usuarios registrados.

