from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Ellipse


class ExemploCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Tamanho da bola
        self.t = dp(50)

        # Desenhar no canvas pelo arquivo .py
        with self.canvas:
            self.bola = Ellipse(pos=(100, 100), size=(self.t, self.t))

        # Atualizar a tela conforme um determinado período de tempo
        # Temos que passar uma função e o período de tempo que essa função será chamada
        Clock.schedule_interval(self.update, 1/60)

    # Dimensões da tela
    def on_size(self, *args):
        self.bola.pos = (self.center_x-self.t/2, self.center_y-self.t/2)

    # Criar a função de atualização da tela
    def update(self, dt):
        # Atualizar a posição da bola
        x, y = self.bola.pos
        self.bola.pos = (x+4, y)


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
