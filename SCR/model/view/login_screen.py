from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from SRC.model.supervisor import Supervisor

class LoginScreen(Screen):
    correo_input = ObjectProperty(None)
    contraseña_input = ObjectProperty(None)
    mensaje = ObjectProperty(None)

    def iniciar_sesion(self):
        correo = self.correo_input.text.strip()
        contraseña = self.contraseña_input.text.strip()
        if correo and contraseña:
            if correo in Supervisor.usuarios and Supervisor.usuarios[correo]["contraseña"] == contraseña:
                Supervisor.usuario_actual = correo
                self.manager.current = "menu_screen"
                self.mensaje.text = ""
            else:
                self.mensaje.text = "Correo o contraseña incorrectos."
        else:
            self.mensaje.text = "Ingrese correo y contraseña."
