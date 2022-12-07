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

        # Velocidade da bola
        self.vx = dp(3)
        self.vy = dp(4)

        # Desenhar no canvas pelo arquivo .py
        with self.canvas:
            self.bola = Ellipse(pos=(100, 100), size=(self.t, self.t))
        Clock.schedule_interval(self.update, 1/60)

    # Dimensões da tela
    def on_size(self, *args):
        self.bola.pos = (self.center_x-self.t/2, self.center_y-self.t/2)

    # Criar a função de atualização da tela
    def update(self, dt):
        # Obter a posição da bola
        x, y = self.bola.pos

        # Obter o tamanho da bola
        t_x, t_y = self.bola.size

        # Obter as dimensões da tela
        l, a = self.width, self.height

        # Alterar a direção da bola no eixo Y
        if y + t_y > self.height:
            self.vy *= -1
        if y <= 0:
            self.vy *= -1

        # Alterar a direção da bola no eixo X
        if x + t_x > self.width:
            self.vx *= -1
        if x <= 0:
            self.vx *= -1

        # Incrementar a velocidade
        x += self.vx
        y += self.vy

        # Atualizar a posição da bola
        self.bola.pos = (x, y)


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
