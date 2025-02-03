class Usuario:
    def __init__(self, dni, nombre, telefono, email, tipo):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.tipo = tipo

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo
