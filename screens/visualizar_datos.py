from kivy.uix.screenmanager import Screen

class visualizar_datosScreen(Screen):
    def go_to_ver_datos_padres(self):
        print('Navigating from Screen visualizar_datos to Screen ver_datos_padres')
        self.manager.current = 'ver_datos_padres'
    def go_to_ver_datos_facturacion(self):
        print('Navigating from Screen visualizar_datos to Screen ver_datos_facturacion')
        self.manager.current = 'ver_datos_facturacion'
    def go_to_inicio(self):
        print('Navigating from Screen visualizar_datos to Screen inicio')
        self.manager.current = 'inicio'