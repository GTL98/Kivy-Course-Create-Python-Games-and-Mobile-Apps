from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


class ExemploCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Desenhar no canvas pelo arquivo .py
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(600, 300, 150, 100), width=5)
            self.rect = Rectangle(pos=(600, 450), size=(150, 100))

    # Criar a função que quando clicar no botão o retângulo anda 10 pixels
    def clique_botao(self):
        # Determinar os eixos X e Y do retângulo
        # Temos que fazer assim pois é uma tupla
        # e como precisamos mudar o valor, é impossível
        # mudar uma tupla
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
