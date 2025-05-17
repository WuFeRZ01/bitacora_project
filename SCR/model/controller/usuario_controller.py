from SRC.model.usuario import Usuario
from SRC.model.errores import ErrorCamposIncompletos, ErrorEmailExistente, ErrorCredenciales
from database.db_config import SessionLocal


class UsuarioController:
    def __init__(self):
        self.db = SessionLocal()

    def registrar_usuario(self, nombre, correo, contraseña):
        if not nombre or not correo or not contraseña:
            raise ErrorCamposIncompletos()

        if self.db.query(Usuario).filter_by(correo=correo).first():
            raise ErrorEmailExistente()

        nuevo = Usuario(nombre=nombre, correo=correo, contraseña=contraseña)
        self.db.add(nuevo)
        self.db.commit()
        return nuevo

    def iniciar_sesion(self, correo, contraseña):
        if not correo or not contraseña:
            raise ErrorCamposIncompletos()

        usuario = self.db.query(Usuario).filter_by(correo=correo, contraseña=contraseña).first()
        if not usuario:
            raise ErrorCredenciales()

        return usuario
