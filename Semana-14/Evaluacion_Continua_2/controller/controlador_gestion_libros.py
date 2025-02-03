from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class ControladorGestionLibros(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz de usuario 
        uic.loadUi('view/gestion_libros.ui', self)

        # Conectar botones a sus respectivas funciones
        self.btn_guardar.clicked.connect(self.guardar_libro)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.btn_buscar.clicked.connect(self.buscar_libro)
        self.btn_editar.clicked.connect(self.editar_libro)
        self.btn_eliminar.clicked.connect(self.eliminar_libro)
        self.btn_cerrar.clicked.connect(self.close)

        # Lista para almacenar los libros 
        self.libros = []

    def guardar_libro(self):
        # Obtener datos de los campos
        isbn = self.le_isbn.text()
        titulo = self.le_titulo.text()
        autor = self.le_autor.text()
        editorial = self.le_editorial.text()
        anio = self.le_anio.text()
        disponibles = self.le_disponibles.text()

        # Validar que no haya campos vacíos
        if not (isbn and titulo and autor and editorial and anio and disponibles):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Agregar libro a la lista
        libro = {
            "ISBN": isbn,
            "Título": titulo,
            "Autor": autor,
            "Editorial": editorial,
            "Año": anio,
            "Disponibles": disponibles,
        }
        self.libros.append(libro)
        self.actualizar_tabla()
        QMessageBox.information(self, "Éxito", "Libro guardado correctamente.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.leISBN.clear()
        self.leTitulo.clear()
        self.leAutor.clear()
        self.leEditorial.clear()
        self.leAnio.clear()
        self.leDisponibles.clear()

    def buscar_libro(self):
        texto_buscar = self.leBuscar.text()
        if not texto_buscar:
            QMessageBox.warning(self, "Error", "Ingrese un término de búsqueda.")
            return

        resultados = [
            libro for libro in self.libros if texto_buscar.lower() in libro["Título"].lower()
        ]

        if resultados:
            self.actualizar_tabla(resultados)
        else:
            QMessageBox.information(self, "Sin resultados", "No se encontraron libros.")

    def editar_libro(self):
        fila_seleccionada = self.tablaLibros.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Error", "Seleccione un libro para editar.")
            return

        # Cargar datos del libro seleccionado en los campos
        libro = self.libros[fila_seleccionada]
        self.leISBN.setText(libro["ISBN"])
        self.leTitulo.setText(libro["Título"])
        self.leAutor.setText(libro["Autor"])
        self.leEditorial.setText(libro["Editorial"])
        self.leAnio.setText(libro["Año"])
        self.leDisponibles.setText(libro["Disponibles"])

        # Eliminar el libro de la lista para que pueda ser actualizado
        del self.libros[fila_seleccionada]
        self.actualizar_tabla()

    def eliminar_libro(self):
        fila_seleccionada = self.tablaLibros.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Error", "Seleccione un libro para eliminar.")
            return

        # Eliminar libro de la lista y actualizar la tabla
        del self.libros[fila_seleccionada]
        self.actualizar_tabla()
        QMessageBox.information(self, "Éxito", "Libro eliminado correctamente.")

    def actualizar_tabla(self, libros=None):
        if libros is None:
            libros = self.libros

        # Limpiar la tabla
        self.tablaLibros.setRowCount(0)

        # Llenar la tabla con los libros
        for libro in libros:
            fila = self.tablaLibros.rowCount()
            self.tablaLibros.insertRow(fila)
            self.tablaLibros.setItem(fila, 0, QTableWidgetItem(libro["ISBN"]))
            self.tablaLibros.setItem(fila, 1, QTableWidgetItem(libro["Título"]))
            self.tablaLibros.setItem(fila, 2, QTableWidgetItem(libro["Autor"]))
            self.tablaLibros.setItem(fila, 3, QTableWidgetItem(libro["Editorial"]))
            self.tablaLibros.setItem(fila, 4, QTableWidgetItem(libro["Año"]))
