

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label


class drop(App):
	def o(self, origen):
		self.dropdownO.select(origen.text)
		self.b2.text=origen.text
		origen=origen.text
		print('Lugar de origen:',origen)

	def d(self, destino):
		self.dropdownD.select(destino.text)
		self.b3.text=destino.text
		destino=destino.text
		print('Lugar de Destino:',destino)


	def build(self):
		self.lista=(["DORADO"], ["ALBROOK"],["LOS ANDES"], ["TOCUMEN"], ["24 DE DICIEMBRE"], ["LAS CUMBRES"])
		self.box = FloatLayout()
		self.l = Label(pos_hint={'x': 0.5/2, 'center_y': 0.9}, size_hint=(0.5, 0.2),text='[color=000080][b][size=35]TARIFAS DE TAXI[/b][/color]',markup = True)
		self.l2 = Label(pos_hint={'x': 0.5/2, 'center_y': 0.7}, size_hint=(0.5, 0.2),text='[color=FF0000][b][size=35][/b][/color]',markup = True)
		self.dropdownO=DropDown()
		self.dropdownD=DropDown()


		for i in self.lista:
			b0=Button(text=i[0], size_hint_y=None, height=30)
			b0.bind(on_release=self.o)
			self.dropdownO.add_widget(b0)

		for t in self.lista:
			b1=Button(text=t[0], size_hint_y=None, height=30)
			b1.bind(on_release=self.d)
			self.dropdownD.add_widget(b1)

		self.b2=Button(pos_hint={'x': 0, 'center_y': .5}, size_hint=(0.5, 0.2),text='[color=ffA500][size=24]LUGAR DE ORIGEN[/color]', markup = True)
		self.b2.bind(on_release=self.dropdownO.open)

		self.b3=Button(pos_hint={'x': 0.5, 'center_y': .5}, size_hint=(0.5, 0.2),text='[color=ffA500][size=24]LUGAR DE DESTINO[/color]', markup = True)
		self.b3.bind(on_release=self.dropdownD.open)

		self.b_calcular=Button(pos_hint={'x': 0.5/2, 'center_y': .1}, size_hint=(0.5, 0.2),text='[color=00ff00][size=24]CALCULAR TARIFA[/color]', markup = True)
		self.b_calcular.bind()

		self.box.add_widget(self.b2)
		self.box.add_widget(self.b3)
		self.box.add_widget(self.b_calcular)
		self.box.add_widget(self.l)


		return self.box

drop().run()