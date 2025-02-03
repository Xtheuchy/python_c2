import sys
from PyQt5.QtWidgets import QApplication
from controller.controlador_login import ControladorLogin
from controller.controlador_principal import ControladorPrincipal


def main():
    app = QApplication(sys.argv)

    # Crear instancia del controlador de login
    login = ControladorLogin()
    login.show()

    # Iniciar el ciclo de eventos
    app.exec_()

    # Verificar si el login fue exitoso
    if login.login_exitoso:
        # Crear instancia del controlador principal
        principal = ControladorPrincipal()
        principal.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
