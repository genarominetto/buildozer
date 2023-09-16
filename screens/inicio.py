from kivy.uix.screenmanager import Screen

class inicioScreen(Screen):
    def go_to_cargar_datos(self):
        print('Navigating from Screen inicio to Screen cargar_datos')
        self.manager.current = 'cargar_datos'
    def go_to_visualizar_datos(self):
        print('Navigating from Screen inicio to Screen visualizar_datos')
        self.manager.current = 'visualizar_datos'