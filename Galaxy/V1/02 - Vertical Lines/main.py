from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


class WidgetPrincipal(Widget):
    # Definir o ponto de perspectiva XY
    ponto_perspectiva_x = NumericProperty(0)
    ponto_perspectiva_y = NumericProperty(0)

    # Definir as linhas verticais
    NUM_LINHAS_V = 7
    ESPACO_LINHAS_V = 0.1  # porcentagem da largura da tela
    linhas_verticais = []

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        self.init_linhas_verticais()

    # Criar uma função para juntar a tela da aplicação com a tela do widget
    def on_parent(self, widget, parent):
        pass

    # Criar uma função para pegar o tamanho da tela da aplicação
    def on_size(self, *args):
        # Devemos chamar a função que atualiza as linhas
        # Se chamarmos a que inicia, o Kivy cria linhas sempre que a tela é redimezionada
        self.atualizar_linhas_verticais()

    # Criar uma função para informar ao Kivy onde está o ponto de perspectica no eixo X
    def on_ponto_perspectiva_x(self, widget, valor):
        print(f'PPX: {valor}')

    # Criar uma função para informar ao Kivy onde está o ponto de perspectica no eixo Y
    def on_ponto_perspectiva_y(self, widget, valor):
        print(f'PPY: {valor}')

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
        offset = -int(self.NUM_LINHAS_V / 2)

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_V):
            linha_x = int(linha_central_x + offset * espacamento)
            self.linhas_verticais[i].points = [linha_x, 0, linha_x, self.height]
            offset += 1


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
