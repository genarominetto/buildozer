from kivy.uix.screenmanager import Screen

class datos_padresScreen(Screen):
    def go_to_cargar_datos(self):
        print('Navigating from Screen datos_padres to Screen cargar_datos')
        self.manager.current = 'cargar_datos'