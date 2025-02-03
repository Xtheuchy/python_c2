class Devolucion:
    def __init__(self, id_devolucion, prestamo, fecha_real, multa=0):
        self.id_devolucion = id_devolucion
        self.prestamo = prestamo
        self.fecha_real = fecha_real
        self.multa = multa

    def get_id_devolucion(self):
        return self.id_devolucion

    def set_id_devolucion(self, id_devolucion):
        self.id_devolucion = id_devolucion

    def get_prestamo(self):
        return self.prestamo

    def set_prestamo(self, prestamo):
        self.prestamo = prestamo

    def get_fecha_real(self):
        return self.fecha_real

    def set_fecha_real(self, fecha_real):
        self.fecha_real = fecha_real

    def get_multa(self):
        return self.multa

    def set_multa(self, multa):
        self.multa = multa

    def procesar_devolucion(self):
        if self.fecha_real > self.prestamo.fecha_devolucion:
            self.multa = self.prestamo.calcular_multa()
        self.prestamo.libro.actualizar_disponibilidad(1)
        print(f"Devolución procesada: {self.prestamo.libro.titulo} por {self.prestamo.usuario.nombre}")
