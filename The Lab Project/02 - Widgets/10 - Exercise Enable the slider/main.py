from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('0')
    contador = 0
    contador_ativado = BooleanProperty(False)

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
    # Com o "id", não precisamos mais criar uma
    # função aqui no aquivo .py
    # O "id" no aquivo .kv já faz isso
    # def switch_ativado(self, widget):
    #     print(f'Switch: {widget.active}')


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
