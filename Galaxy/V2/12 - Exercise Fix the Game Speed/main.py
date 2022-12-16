# Importar isso daqui antes de tudo para que toda a aplicação fique no tamanho desejado
from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

import random
from kivy.app import App
from kivy import platform
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Quad
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Triangle


class WidgetPrincipal(Widget):
    # Importar os módulos criados
    from transformacoes import transformar, transformar_2D, transformar_perspectiva
    from interacao_usuario import (on_touch_up, on_touch_down, on_keyboard_up,
                                   on_keyboard_down, keyboard_closed)

    # Definir o ponto de perspectiva XY
    ponto_perspectiva_x = NumericProperty(0)
    ponto_perspectiva_y = NumericProperty(0)

    # Definir as linhas verticais
    NUM_LINHAS_V = 8
    ESPACO_LINHAS_V = 0.4  # porcentagem da largura da tela
    linhas_verticais = []

    # Definir as linhas horizontais
    NUM_LINHAS_H = 15
    ESPACO_LINHAS_H = 0.1  # porcentagem da altura da tela
    linhas_horizontais = []

    # Definir a taxa que as linhas horizontais se moverão
    VELOCIDADE_Y = 0.8
    offset_atual_y = 0
    loop_atual_y = 0

    # Definir a taxa que as linhas verticais se moverão
    VELOCIDADE_X = 3
    velocidade_atual_x = 0
    offset_atual_x = 0

    # Configurações dos tiles
    NUM_TILES = 16
    tiles = []
    coord_tiles = []

    # Configurações da nave
    ALTURA_NAVE = 0.025
    LARGURA_NAVE = 0.05
    BASE_Y_NAVE = 0.04
    nave = None

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        self.init_linhas_verticais()
        self.init_linhas_horizontais()
        self.init_tiles()
        self.init_nave()
        self.pre_tiles_coord()
        self.gerar_tiles_coord()

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

    # Criar a função para a inicialização da nave
    def init_nave(self):
        with self.canvas:
            Color(0, 0, 0)
            self.nave = Triangle()

    # Criar a função que atualiza a posição da nave
    def atualizar_nave(self):
        center_x = self.width / 2
        base_y = self.BASE_Y_NAVE * self.height
        altura_nave = self.ALTURA_NAVE * self.height
        largura_metade_nave = self.LARGURA_NAVE * self.width
        # Ordem dos dos pontos:
        #   2
        # 1   3
        x1, y1 = self.transformar(center_x - largura_metade_nave, base_y)
        x2, y2 = self.transformar(center_x, base_y + altura_nave)
        x3, y3 = self.transformar(center_x + largura_metade_nave, base_y)
        self.nave.points = [x1, y1, x2, y2, x3, y3]

    # Criar uma função para a inicialização dos tiles
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NUM_TILES):
                self.tiles.append(Quad())

    # Criar a função que começa o jogo com 10 tiles em linha reta
    def pre_tiles_coord(self):
        for i in range(0, 10):
            self.coord_tiles.append((0, i))

    # Criar a função que gera os tiles
    def gerar_tiles_coord(self):
        ultimo_x = 0
        ultimo_y = 0

        # Remover os tiles que saíram da tela
        for i in range(len(self.coord_tiles)-1, -1, -1):
            if self.coord_tiles[i][1] < self.loop_atual_y:
                del self.coord_tiles[i]

        if len(self.coord_tiles) > 0:
            ultimas_coords = self.coord_tiles[-1]
            ultimo_x = ultimas_coords[0]
            ultimo_y = ultimas_coords[1] + 1

        for i in range(len(self.coord_tiles), self.NUM_TILES):
            # r == 0: Linha reta
            # r == 1: Direita
            # r == 2: Esquerda
            r = random.randint(0, 2)

            # Evitar que os tiles saiam do mapa
            indice_comeco = -int(self.NUM_LINHAS_V / 2) + 1
            indice_final = indice_comeco + self.NUM_LINHAS_V - 1
            if ultimo_x <= indice_comeco:
                r = 1
            if ultimo_x >= indice_final:
                r = 2

            self.coord_tiles.append((ultimo_x, ultimo_y))
            if r == 1:
                ultimo_x += 1
                self.coord_tiles.append((ultimo_x, ultimo_y))
                ultimo_y += 1
                self.coord_tiles.append((ultimo_x, ultimo_y))
            if r == 2:
                ultimo_x -= 1
                self.coord_tiles.append((ultimo_x, ultimo_y))
                ultimo_y += 1
                self.coord_tiles.append((ultimo_x, ultimo_y))
            ultimo_y += 1

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
        ti_y -= self.loop_atual_y  # isso permite que o tile vá até o final da tela (bottom)
        x = self.obter_linha_x_de_indice(ti_x)
        y = self.obter_linha_y_de_indice(ti_y)

        return x, y

    # Função para atualizar o tiles
    def atualizar_tile(self):
        for i in range(0, self.NUM_TILES):
            tile = self.tiles[i]
            coords_tile = self.coord_tiles[i]
            x_min, y_min = self.obter_coord_tile(coords_tile[0], coords_tile[1])
            x_max, y_max = self.obter_coord_tile(coords_tile[0]+1, coords_tile[1]+1)

            # Obter os pontos para o "Quad()"
            # Ordem:
            # 2 --- 3
            # |     |
            # 1 --- 4
            x1, y1 = self.transformar(x_min, y_min)
            x2, y2 = self.transformar(x_min, y_max)
            x3, y3 = self.transformar(x_max, y_max)
            x4, y4 = self.transformar(x_max, y_min)
            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

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
        self.atualizar_nave()

        # Deixar a velocidade dependente da altura da tela
        # Desse modo, em qualquer dimensão a velocidade é constante
        velocidade_y = self.VELOCIDADE_Y * self.height / 100
        self.offset_atual_y += velocidade_y * fator_tempo

        # Verificar se a linha já saiu da tela, se saiu então adicionar uma linha
        # horizontal no ponto de perspectiva
        espacamento_y = self.ESPACO_LINHAS_H * self.height
        if self.offset_atual_y >= espacamento_y:
            self.offset_atual_y -= espacamento_y
            self.loop_atual_y += 1
            self.gerar_tiles_coord()

        # Deixar a velocidade dependente da largura da tela
        # Desse modo, em qualquer dimensão a velocidade é constante
        velocidade_x = self.velocidade_atual_x * self.width / 100
        self.offset_atual_x += velocidade_x * fator_tempo


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
