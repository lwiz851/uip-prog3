__author__ = 'luis M'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.graphics.vertex_instructions import *
from kivy.graphics.context_instructions import *


Builder.load_string('''
<MenuScreen>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'TARIFAS DE TAXIS'
			font_size: '30sp'

		Button:
			text: 'Sector Sur'
			color: 0, 0, 1, 1
			font_size: '24sp'
			text_size: self.size
			halign: 'center'
			valign: 'middle'
			size_hint: 1, 1
			on_press: root.manager.current = 'sector_sur'

		Button:
			text: 'Sector Norte'
			color: 0, 0, 1, 1
			font_size: '24sp'
			text_size: self.size
			halign: 'center'
			valign: 'middle'
			size_hint: 1, 1
			on_press: root.manager.current = 'sector_norte'


<Sector_sur>:
	GridLayout:
		cols: 2
		Label:
			text: 'Seleccione Sector de Partida'
		TextInput:
			id: sector_p
		Label:
			text: 'Seleccione Sector de Destino'
		TextInput:
			id: sector_d
		Button:
			text: 'Regresar al menu'
			on_press: root.manager.current = 'menu'
		Button:
			text: 'Calcular Precio de Servicio'
			on_press: app.calcular_p(sector_p.text, sector_d.text)

<Sector_norte>:
	GridLayout:
		cols: 2
		Label:
			text: 'Seleccione Sector de Partida'
		TextInput:
			id: sector_p
		Label:
			text: 'Seleccione Sector de Destino'
		TextInput:
			id: sector_d
		Button:
			text: 'Regresar al menu'
			on_press: root.manager.current = 'menu'
		Button:
			text: 'Calcular Precio de Servicio'
			on_press: app.calcular_p(sector_p.text, sector_d.text)

''')


class MenuScreen(Screen):
	pass

class Sector_sur(Screen):
	pass

class Sector_norte(Screen):
	pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Sector_sur(name='sector_sur'))
sm.add_widget(Sector_norte(name='sector_norte'))


class PrincipalApp(App):

	def build(self):
		return sm


if __name__ == '__main__':
    PrincipalApp().run()