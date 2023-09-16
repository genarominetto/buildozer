from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition

# Load KV files
Builder.load_file('kv/inicio.kv')
Builder.load_file('kv/cargar_datos.kv')
Builder.load_file('kv/visualizar_datos.kv')
Builder.load_file('kv/datos_padres.kv')
Builder.load_file('kv/datos_facturacion.kv')
Builder.load_file('kv/ver_datos_padres.kv')
Builder.load_file('kv/ver_datos_facturacion.kv')

from screens.inicio import inicioScreen
from screens.cargar_datos import cargar_datosScreen
from screens.visualizar_datos import visualizar_datosScreen
from screens.datos_padres import datos_padresScreen
from screens.datos_facturacion import datos_facturacionScreen
from screens.ver_datos_padres import ver_datos_padresScreen
from screens.ver_datos_facturacion import ver_datos_facturacionScreen

class MainApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        inicio_screen = inicioScreen(name='inicio')
        sm.add_widget(inicio_screen)
        cargar_datos_screen = cargar_datosScreen(name='cargar_datos')
        sm.add_widget(cargar_datos_screen)
        visualizar_datos_screen = visualizar_datosScreen(name='visualizar_datos')
        sm.add_widget(visualizar_datos_screen)
        datos_padres_screen = datos_padresScreen(name='datos_padres')
        sm.add_widget(datos_padres_screen)
        datos_facturacion_screen = datos_facturacionScreen(name='datos_facturacion')
        sm.add_widget(datos_facturacion_screen)
        ver_datos_padres_screen = ver_datos_padresScreen(name='ver_datos_padres')
        sm.add_widget(ver_datos_padres_screen)
        ver_datos_facturacion_screen = ver_datos_facturacionScreen(name='ver_datos_facturacion')
        sm.add_widget(ver_datos_facturacion_screen)
        sm.current = 'inicio'
        return sm

if __name__ == '__main__':
    MainApp().run()