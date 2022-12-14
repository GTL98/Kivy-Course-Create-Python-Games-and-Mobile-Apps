from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty


class WidgetPrincipal(Widget):
    # Definir o ponto de perspectiva XY
    ponto_perspectiva_x = NumericProperty(0)
    ponto_perspectiva_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        print(f'''Widget:
    Largura: {self.width}
    Altura: {self.height}''')

    # Criar uma função para juntar a tela da aplicação com a tela do widget
    def on_parent(self, widget, parent):
        pass

    # Criar uma função para pegar o tamanho da tela da aplicação
    def on_size(self, *args):
        print(f'''on_size:
    Largura: {self.width}
    Altura: {self.height}''')

    # Criar uma função para informar ao Kivy onde está o ponto de perspectica no eixo X
    def on_ponto_perspectiva_x(self, widget, valor):
        print(f'PPX: {valor}')

    # Criar uma função para informar ao Kivy onde está o ponto de perspectica no eixo Y
    def on_ponto_perspectiva_y(self, widget, valor):
        print(f'PPY: {valor}')


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
