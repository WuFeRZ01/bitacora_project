class ErrorSesionNoIniciada(Exception):
    def __init__(self):
        super().__init__("Debe iniciar sesión primero.")


class ErrorCamposIncompletos(Exception):
    def __init__(self):
        super().__init__("Todos los campos son obligatorios.")


class ErrorEmailExistente(Exception):
    def __init__(self):
        super().__init__("El correo ya está registrado.")


class ErrorCredenciales(Exception):
    def __init__(self):
        super().__init__("Correo o contraseña incorrectos.")
