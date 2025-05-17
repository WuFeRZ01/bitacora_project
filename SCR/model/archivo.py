from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db_config import Base


class Archivo(Base):
    __tablename__ = "archivos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    ruta = Column(String, nullable=False)
    actividad_id = Column(Integer, ForeignKey("actividades.id"))

    actividad = relationship("Actividad", back_populates="archivos")
