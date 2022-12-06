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

    def clique_botao(self):
        x, y = self.rect.pos

        # Obter os valores da largura e altura do retângulo
        lar, alt = self.rect.size

        # Informar qual a taxa de incremento
        incremento = dp(10)

        # Saber distância entre o retângulo até a borda
        diferenca = self.width - (x + lar)

        # Verificar se ainda há espaço para mover
        if diferenca < incremento:
            # Fazer isso quando a diferença for menor do que o incremento
            # Fazendo isso, o retângulo andará somete o quanto falta para chegar na borda
            incremento = diferenca

        # Aumentar o valor de x
        x += incremento

        # Mover o retângulo
        self.rect.pos = (x, y)


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
