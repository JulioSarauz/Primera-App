import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics','width',400)
Config.set('graphics','height',400)

class Contenedor_01(BoxLayout):
    None
class appApp(App):
    title="Hola Mundo"
    def build(self):
        return Contenedor_01()

if __name__ == '__main__':
    appApp().run()