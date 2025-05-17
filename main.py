from kivy.app import App
from kivy.lang import Builder
from SRC.view.login_screen import LoginScreen
from kivy.uix.screenmanager import ScreenManager

class BitacoraApp(App):
    def build(self):
        Builder.load_file("SRC/view/main.kv")
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm

if __name__ == "__main__":
    BitacoraApp().run()
