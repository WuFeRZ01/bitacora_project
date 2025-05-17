from kivy.uix.screenmanager import Screen
from SRC.model.actividad import Actividad
from SRC.model.supervisor import Reporte, Supervisor

class MenuScreen(Screen):

    def registrar_actividad(self):
        try:
            Actividad.registrar_actividad()
        except Exception as e:
            print(f"Error: {e}")

    def consultar_actividades(self):
        try:
            Actividad.consultar_actividad()
        except Exception as e:
            print(f"Error: {e}")

    def generar_reporte(self):
        try:
            Reporte.generar_reporte()
        except Exception as e:
            print(f"Error: {e}")

    def cerrar_sesion(self):
        Supervisor.usuario_actual = None
        self.manager.current = "login_screen"
