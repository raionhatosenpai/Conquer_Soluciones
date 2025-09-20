# Crea una clase "Libro" con atributos como título, autor y año de publicación. 
# Luego, crea varios objetos Libro y muestra su información.

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = año_publicacion

    def details(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"
    
# Solicitar datos al usuario
libros = []

while True:
    titulo = input("Ingrese el título del libro (o 'salir' para terminar): ").title()
    if titulo.lower() == "salir":
        break
    autor = input("Ingrese el autor del libro: ").title()
    año_publicacion = int(input("Ingrese el año de publicación del libro: "))
    
    libro = Libro(titulo, autor, año_publicacion)
    libros.append(libro)

# Mostrar todos los libros registrados
print("\nLibros registrados:")
for libro in libros:
    print(libro.details())

# Ejemplos
# Cien años de soledad, Gabriel García Márquez, 1967
# Don Quijote de la Mancha, Miguel de Cervantes, 1605
# Los hermanos Karamazov, Fiódor Dostoyevski, 1880
# El amor en los tiempos del cólera, Gabriel García Márquez, 1985
# La Odisea, Homero, -800