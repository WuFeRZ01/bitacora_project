import pytest
from SRC.model.actividad import Actividad, Archivo
from datetime import datetime

def test_crear_archivo():
    archivo = Archivo("informe.pdf", "pdf", "/docs/informe.pdf")
    assert archivo.Nombre == "informe.pdf"
    assert archivo.Tipo == "pdf"
    assert archivo.Ruta == "/docs/informe.pdf"

def test_registrar_actividad_valida():
    
    anexos = [Archivo("foto.jpg", "jpg", "/fotos/foto.jpg")]
    supervisor = None  
    actividad = Actividad(1, datetime.now(), "Juan", "Inspección diaria", "Soleado", anexos, supervisor)
    assert actividad.Descripcion == "Inspección diaria"
