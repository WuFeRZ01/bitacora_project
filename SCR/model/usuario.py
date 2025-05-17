from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_config import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)

    actividades = relationship("Actividad", back_populates="usuario")
