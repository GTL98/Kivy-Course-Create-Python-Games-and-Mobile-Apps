# Importar isso daqui antes de tudo para que toda a aplicação fique no tamanho desejado
from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy import platform
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


class WidgetPrincipal(Widget):
    # Importar os módulos criados
    from transformacoes import transformar, transformar_2D, transformar_perspectiva
    from interacao_usuario import (on_touch_up, on_touch_down, on_keyboard_up,
                                   on_keyboard_down, keyboard_closed)

    # Definir o ponto de perspectiva XY
    ponto_perspectiva_x = NumericProperty(0)
    ponto_perspectiva_y = NumericProperty(0)

    # Definir as linhas verticais
    NUM_LINHAS_V = 10
    ESPACO_LINHAS_V = 0.25  # porcentagem da largura da tela
    linhas_verticais = []

    # Definir as linhas horizontais
    NUM_LINHAS_H = 15
    ESPACO_LINHAS_H = 0.1  # porcentagem da altura da tela
    linhas_horizontais = []

    # Definir a taxa que as linhas horizontais se moverão
    VELOCIDADE_Y = 2
    offset_atual_y = 0

    # Definir a taxa que as linhas verticais se moverão
    VELOCIDADE_X = 12
    velocidade_atual_x = 0
    offset_atual_x = 0

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        self.init_linhas_verticais()
        self.init_linhas_horizontais()

        if self.eh_desktop():
            # Iniciar as funções da captura de teclas para o Kivy
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.atualizar, 1/60)

    # Criar a função que determina se a plataforma é DESKTOP ou MOBILE
    def eh_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    # Criar uma função para a inicialização das linhas verticais
    def init_linhas_verticais(self):
        with self.canvas:
            Color(1, 1, 1)

            # Criar as linhas
            for i in range(0, self.NUM_LINHAS_V):
                self.linhas_verticais.append(Line())

    # Criar uma função para atualizar as linhas verticais
    def atualizar_linhas_verticais(self):
        linha_central_x = int(self.width / 2)
        espacamento = self.ESPACO_LINHAS_V * self.width

        # Informar o desvio (offset) para que as linhas sejam colocadas em relação ao centro
        # de modo equidistante
        offset = -int(self.NUM_LINHAS_V / 2) + 0.5

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_V):
            linha_x = linha_central_x + offset * espacamento + self.offset_atual_x

            # Transformar as linhas
            x1, y1 = self.transformar(linha_x, 0)
            x2, y2 = self.transformar(linha_x, self.height)

            self.linhas_verticais[i].points = [x1, y1, x2, y2]
            offset += 1

    # Criar uma função para a inicialização das linhas horizontais
    def init_linhas_horizontais(self):
        with self.canvas:
            Color(1, 1, 1)

            # Criar as linhas
            for i in range(0, self.NUM_LINHAS_H):
                self.linhas_horizontais.append(Line())

    # Criar uma função para atualizar as linhas horizontais
    def atualizar_linhas_horizontais(self):
        # Determinar onde começa e terminas as linhas verticais para
        # que possamos colocar as linhas horizontais entre essas linhas
        # verticais
        linha_central_x = int(self.width / 2)
        espacamento = self.ESPACO_LINHAS_V * self.width
        offset = int(self.NUM_LINHAS_V / 2) - 0.5
        x_min = linha_central_x - offset * espacamento + self.offset_atual_x
        x_max = linha_central_x + offset * espacamento + self.offset_atual_x
        espacamento_y = self.ESPACO_LINHAS_H * self.height

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_H):
            linha_y = i * espacamento_y - self.offset_atual_y

            # Transformar as linhas
            x1, y1 = self.transformar(x_min, linha_y)
            x2, y2 = self.transformar(x_max, linha_y)

            self.linhas_horizontais[i].points = [x1, y1, x2, y2]

    # Criar a função que atualiza a tela
    def atualizar(self, delta):
        self.fator_tempo = delta * 60  # isso aqui permite que o FPS fique certo em qualquer dispositivo
        self.atualizar_linhas_verticais()
        self.atualizar_linhas_horizontais()
        self.offset_atual_y += self.VELOCIDADE_Y * self.fator_tempo

        # Verificar se a linha já saiu da tela, se saiu então adicionar uma linha
        # horizontal no ponto de perspectiva
        espacamento_y = self.ESPACO_LINHAS_H * self.height
        if self.offset_atual_y >= espacamento_y:
            self.offset_atual_y -= espacamento_y

        self.offset_atual_x += self.velocidade_atual_x * self.fator_tempo


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
