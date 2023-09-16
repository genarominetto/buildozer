from kivy.uix.screenmanager import Screen

class cargar_datosScreen(Screen):
    def go_to_datos_padres(self):
        print('Navigating from Screen cargar_datos to Screen datos_padres')
        self.manager.current = 'datos_padres'
    def go_to_datos_facturacion(self):
        print('Navigating from Screen cargar_datos to Screen datos_facturacion')
        self.manager.current = 'datos_facturacion'
    def go_to_inicio(self):
        print('Navigating from Screen cargar_datos to Screen inicio')
        self.manager.current = 'inicio'