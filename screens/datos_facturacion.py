from kivy.uix.screenmanager import Screen

class datos_facturacionScreen(Screen):
    def go_to_cargar_datos(self):
        print('Navigating from Screen datos_facturacion to Screen cargar_datos')
        self.manager.current = 'cargar_datos'