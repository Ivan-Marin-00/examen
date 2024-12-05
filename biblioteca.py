class Usuario:
    def __init__(self, id_user, nombre, direccion):
        # Encapsulamiento
        self.id_user = id_user
        self.nombre = nombre
        self.direccion = direccion


class Categoria:
    def __init__(self, nombre, autor, id_libro):
        # Encapsulamiento
        self.nombre = nombre
        self.autor = autor
        self.id_libro = id_libro
        self.libros = [] 

    def agregar_libro(self, libro):
        self.libros.append(libro)  


class LibrosDisponible:
    def __init__(self, id_libro, autor, disponible):
        self.id_libro = id_libro
        self.autor = autor
        self.disponible = disponible  

    def buscar_disponible(self):
        return self.disponible


class Prestamos:
    def __init__(self, id_user, id_libro):
        self.id_user = id_user
        self.id_libro = id_libro

    def validar_prestamo(self, libro):
        # USO DE EXEPCIONES CON UN BLOQUE TRY CATCH
        try:
            if libro is None:
                raise ValueError("El libro proporcionado no existe.")  
            if libro.buscar_disponible():
                libro.disponible = False  
                print("Préstamo exitoso. El libro ahora no está disponible.")
                return True
            else:
                print("Préstamo fallido. El libro no está disponible.")
                return False
        except ValueError as e:
            print(f"Error en el préstamo: {e}")
            return False


if __name__ == "__main__":


#EJEMPLO DE USO
    # Se crea un usuario
    usuario = Usuario(1, "Ivan", "Atlacomulco")

    # Se crea una categoría y libros
    categoria = Categoria("Ciencia Ficción", "Isaac Asimov", 101)
    libro1 = LibrosDisponible(101, "Isaac Asimov", True)
    categoria.agregar_libro(libro1)

    # Mostrar estado inicial del libro
    print(f"Estado inicial del libro: {'Disponible' if libro1.buscar_disponible() else 'No Disponible'}")

    # Realizar un préstamo
    prestamo = Prestamos(usuario.id_user, libro1.id_libro)
    prestamo.validar_prestamo(libro1)

    # Mostrar estado final del libro
    print(f"Estado final del libro: {'Disponible' if libro1.buscar_disponible() else 'No Disponible'}")


