from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.db_config import Base


class Actividad(Base):
    __tablename__ = 'actividades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    responsable = Column(String, nullable=False)
    condiciones_climaticas = Column(String, nullable=True)
    fecha_hora = Column(DateTime, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="actividades")
    archivos = relationship("Archivo", back_populates="actividad")
