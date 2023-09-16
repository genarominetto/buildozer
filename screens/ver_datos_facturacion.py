from kivy.uix.screenmanager import Screen

class ver_datos_facturacionScreen(Screen):
    def go_to_visualizar_datos(self):
        print('Navigating from Screen ver_datos_facturacion to Screen visualizar_datos')
        self.manager.current = 'visualizar_datos'