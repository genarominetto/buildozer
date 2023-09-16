from kivy.uix.screenmanager import Screen

class ver_datos_padresScreen(Screen):
    def go_to_visualizar_datos(self):
        print('Navigating from Screen ver_datos_padres to Screen visualizar_datos')
        self.manager.current = 'visualizar_datos'