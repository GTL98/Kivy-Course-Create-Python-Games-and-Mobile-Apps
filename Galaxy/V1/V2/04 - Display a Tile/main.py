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
from kivy.graphics.vertex_instructions import Quad
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
    NUM_LINHAS_V = 4
    ESPACO_LINHAS_V = 0.1  # porcentagem da largura da tela
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

    # Configurações dos tiles
    tile = None
    ti_x = 1
    ti_y = 2

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        self.init_linhas_verticais()
        self.init_linhas_horizontais()
        self.init_tiles()

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

    # Criar uma função para a inicialização dos tiles
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            self.tile = Quad()

    # Criar uma função para a inicialização das linhas verticais
    def init_linhas_verticais(self):
        with self.canvas:
            Color(1, 1, 1)

            # Criar as linhas
            for i in range(0, self.NUM_LINHAS_V):
                self.linhas_verticais.append(Line())

    # Função que obtêm a linha do eixo X a partir do índice
    def obter_linha_x_de_indice(self, indice):
        linha_central_x = self.ponto_perspectiva_x
        espacamento = self.ESPACO_LINHAS_V * self.width
        offset = indice - 0.5
        linha_x = linha_central_x + offset * espacamento + self.offset_atual_x

        return linha_x

    # Função que obtêm a linha do eixo Y a partir do índice
    def obter_linha_y_de_indice(self, indice):
        espacamento_y = self.ESPACO_LINHAS_H * self.height
        linha_y = indice * espacamento_y - self.offset_atual_y

        return linha_y

    # Função que obtêm os quatro pontos do quadrado para colocar o tile
    def obter_coord_tile(self, ti_x, ti_y):
        x = self.obter_linha_x_de_indice(ti_x)
        y = self.obter_linha_y_de_indice(ti_y)

        return x, y

    # Função para atualizar o tiles
    def atualizar_tile(self):
        x_min, y_min = self.obter_coord_tile(self.ti_x, self.ti_y)
        x_max, y_max = self.obter_coord_tile(self.ti_x+1, self.ti_y+1)

        # Obter os pontos para o "Quad()"
        # Ordem:
        # 2 --- 3
        # |     |
        # 1 --- 4
        x1, y1 = self.transformar(x_min, y_min)
        x2, y2 = self.transformar(x_min, y_max)
        x3, y3 = self.transformar(x_max, y_max)
        x4, y4 = self.transformar(x_max, y_min)
        self.tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    # Criar uma função para atualizar as linhas verticais
    def atualizar_linhas_verticais(self):
        # Informar a posição das linhas na tela
        indice_comeco = -int(self.NUM_LINHAS_V / 2) + 1
        indice_final = indice_comeco + self.NUM_LINHAS_V
        for i in range(indice_comeco, indice_final):
            linha_x = self.obter_linha_x_de_indice(i)

            # Transformar as linhas
            x1, y1 = self.transformar(linha_x, 0)
            x2, y2 = self.transformar(linha_x, self.height)

            self.linhas_verticais[i].points = [x1, y1, x2, y2]

    # Criar uma função para a inicialização das linhas horizontais
    def init_linhas_horizontais(self):
        with self.canvas:
            Color(1, 1, 1)

            # Criar as linhas
            for i in range(0, self.NUM_LINHAS_H):
                self.linhas_horizontais.append(Line())

    # Criar uma função para atualizar as linhas horizontais
    def atualizar_linhas_horizontais(self):
        indice_comeco = -int(self.NUM_LINHAS_V / 2) + 1
        indice_final = indice_comeco + self.NUM_LINHAS_V - 1
        x_min = self.obter_linha_x_de_indice(indice_comeco)
        x_max = self.obter_linha_x_de_indice(indice_final)

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_H):
            linha_y = self.obter_linha_y_de_indice(i)

            # Transformar as linhas
            x1, y1 = self.transformar(x_min, linha_y)
            x2, y2 = self.transformar(x_max, linha_y)

            self.linhas_horizontais[i].points = [x1, y1, x2, y2]

    # Criar a função que atualiza a tela
    def atualizar(self, delta):
        fator_tempo = delta * 60  # isso aqui permite que o FPS fique certo em qualquer dispositivo
        self.atualizar_linhas_verticais()
        self.atualizar_linhas_horizontais()
        self.atualizar_tile()
        # self.offset_atual_y += self.VELOCIDADE_Y * fator_tempo

        # Verificar se a linha já saiu da tela, se saiu então adicionar uma linha
        # horizontal no ponto de perspectiva
        espacamento_y = self.ESPACO_LINHAS_H * self.height
        if self.offset_atual_y >= espacamento_y:
            self.offset_atual_y -= espacamento_y

        # self.offset_atual_x += self.velocidade_atual_x * fator_tempo


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
