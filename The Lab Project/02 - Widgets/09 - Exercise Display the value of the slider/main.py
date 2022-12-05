from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


class ExemploWidgets(GridLayout):
    meu_texto = StringProperty('0')
    contador = 0
    contador_ativado = BooleanProperty(False)
    #texto_slider = StringProperty('Valor')

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

    def switch_ativado(self, widget):
        print(f'Switch: {widget.active}')
    # Não é mais necessário utilizar essa função
    # pois utilizamos o "id" no arquivo .kv, que
    # faz a mesma coisa que essa função
    # def obter_valor_slider(self, widget):
    #     self.valor_slider = int(widget.value)
    #     self.texto_slider = str(self.valor_slider)


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
