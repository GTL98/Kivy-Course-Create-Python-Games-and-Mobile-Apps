from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('Olá!')

    def clique_botao(self):
        print('Botão clicado')
        self.meu_texto = 'Você clicou!'


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
