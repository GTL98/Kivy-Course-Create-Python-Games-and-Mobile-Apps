from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('0')
    contador = 0

    def clique_botao(self):
        self.contador += 1
        self.meu_texto = f'{self.contador}'


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
