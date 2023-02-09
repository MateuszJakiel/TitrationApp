from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class WindowManager(ScreenManager):

    class MainWindow(Screen):

        def test(self):
            if float(self.ids.R.text) * float(self.ids.s.text) <= 0:
                invalidData()
            else:
                pass

    class WindowV(Screen):

        def change_place(self):
            screen2 = self.manager.get_screen('main')
            if float(self.ids.m.text):
                if float(screen2.ids._result.text) > 0:
                    math = str(float(self.ids.m.text) / float(screen2.ids._result.text))
                    return math
            invalidData()

    class WindowX(Screen):

        def change_place2(self):
            screen2 = self.manager.get_screen('main')
            if float(self.ids.V.text):
                if screen2.ids._result.text:
                    if self.ids.m2.text > 0:
                        math = str(float(self.ids.V.text) * float(screen2.ids._result.text) / float(self.ids.m2.text) * 100)
                        return math
            invalidData()


def invalidData():
    pop = Popup(title='Źle wpisane dane', content=Label(text='Źle wpisano dane.'),
      size_hint=(None, None),
      size=(400, 400))
    pop.open()


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'


MyApp().run()
