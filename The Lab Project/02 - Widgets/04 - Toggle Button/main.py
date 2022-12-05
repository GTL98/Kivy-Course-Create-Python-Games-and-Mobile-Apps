from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('0')
    contador = 0

    def clique_botao(self):
        self.contador += 1
        self.meu_texto = f'{self.contador}'

    def estado_botao_toggle(self, widget):
        print(f'Estado do toggle: {widget.state}')
        # Mudar o texto do botão
        # Como já temos acesso ao widget, não precisamos
        # atribuir um StringProperty(), podemos alterar
        # o texto diretamente pelas propriedades do widget
        if widget.state == 'normal':
            # Desligado
            widget.text = 'OFF'
        else:
            # Ligado
            widget.text = 'ON'


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
