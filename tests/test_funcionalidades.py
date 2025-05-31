import unittest
from SCR.supervisor import Supervisor
from SCR.actividad import Actividad

class TestFuncionalidades(unittest.TestCase):

    def setUp(self):
        self.supervisor = Supervisor()

    def test_agregar_y_listar_actividad(self):
        act = Actividad("Inspección", "Revisar cimentación", "2025-06-01")
        self.supervisor.agregar_actividad(act)
        actividades = self.supervisor.listar_actividades()
        self.assertEqual(len(actividades), 1)
        self.assertEqual(actividades[0].nombre, "Inspección")

    def test_eliminar_actividad(self):
        act1 = Actividad("Act1", "Desc1", "2025-06-01")
        act2 = Actividad("Act2", "Desc2", "2025-06-02")
        self.supervisor.agregar_actividad(act1)
        self.supervisor.agregar_actividad(act2)
        self.supervisor.eliminar_actividad(0)
        actividades = self.supervisor.listar_actividades()
        self.assertEqual(len(actividades), 1)
        self.assertEqual(actividades[0].nombre, "Act2")

    def test_agregar_y_listar_usuario(self):
        usuario = {"nombre": "Juan", "rol": "Ingeniero"}
        self.supervisor.agregar_usuario(usuario)
        usuarios = self.supervisor.listar_usuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['nombre'], "Juan")

    def test_eliminar_usuario(self):
        self.supervisor.agregar_usuario({"nombre": "A", "rol": "R"})
        self.supervisor.eliminar_usuario(0)
        usuarios = self.supervisor.listar_usuarios()
        self.assertEqual(len(usuarios), 0)

if __name__ == '__main__':
    unittest.main()