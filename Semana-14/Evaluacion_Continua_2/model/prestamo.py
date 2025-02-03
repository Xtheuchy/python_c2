from datetime import datetime

class Prestamo:
    def __init__(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def get_id_prestamo(self):
        return self.id_prestamo

    def set_id_prestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_libro(self):
        return self.libro

    def set_libro(self, libro):
        self.libro = libro

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def get_fecha_devolucion(self):
        return self.fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    def registrar_prestamo(self):
        print(f"Prestamo registrado: {self.id_prestamo} - {self.libro.titulo} a {self.usuario.nombre}")

    def calcular_multa(self):
        fecha_actual = datetime.now()
        if fecha_actual > self.fecha_devolucion:
            dias_tarde = (fecha_actual - self.fecha_devolucion).days
            multa = dias_tarde * 1  
            return multa
        return 0
