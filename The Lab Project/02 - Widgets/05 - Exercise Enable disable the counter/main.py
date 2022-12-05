from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('0')
    contador = 0
    # Usaremos uma tag para determinar se o botão
    # ficará ativado ou não
    contador_ativado = False

    def clique_botao(self):
        if self.contador_ativado:
            self.contador += 1
            self.meu_texto = f'{self.contador}'

    def estado_botao_toggle(self, widget):
        if widget.state == 'normal':
            widget.text = 'OFF'
            self.contador_ativado = False
        else:
            widget.text = 'ON'
            self.contador_ativado = True


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
