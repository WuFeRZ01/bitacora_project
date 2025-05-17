from SRC.model.actividad import Actividad
from SRC.model.archivo import Archivo
from database.db_config import SessionLocal
from datetime import datetime


class ActividadController:
    def __init__(self, usuario_id):
        self.db = SessionLocal()
        self.usuario_id = usuario_id

    def crear_actividad(self, descripcion, responsable, condiciones, fecha_hora):
        actividad = Actividad(
            descripcion=descripcion,
            responsable=responsable,
            condiciones_climaticas=condiciones,
            fecha_hora=fecha_hora,
            usuario_id=self.usuario_id
        )
        self.db.add(actividad)
        self.db.commit()
        return actividad

    def agregar_archivo(self, actividad_id, nombre, tipo, ruta):
        archivo = Archivo(
            nombre=nombre,
            tipo=tipo,
            ruta=ruta,
            actividad_id=actividad_id
        )
        self.db.add(archivo)
        self.db.commit()
        return archivo

    def listar_actividades(self):
        return self.db.query(Actividad).filter_by(usuario_id=self.usuario_id).all()
