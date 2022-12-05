from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('Você clicou 0 vezes!')
    contador = 0

    def clique_botao(self):
        self.contador += 1
        self.meu_texto = f'Você clicou {self.contador} vezes!'


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
