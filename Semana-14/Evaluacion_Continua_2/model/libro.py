class Libro:
    def __init__(self, isbn, titulo, autor, editorial, anio, disponibles):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
        self.disponibles = disponibles

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_editorial(self):
        return self.editorial

    def set_editorial(self, editorial):
        self.editorial = editorial

    def get_anio(self):
        return self.anio

    def set_anio(self, anio):
        self.anio = anio

    def get_disponibles(self):
        return self.disponibles

    def set_disponibles(self, disponibles):
        self.disponibles = disponibles

    def actualizar_disponibilidad(self, cantidad):
        self.disponibles += cantidad
