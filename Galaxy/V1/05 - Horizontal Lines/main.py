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
    NUM_LINHAS_V = 10
    ESPACO_LINHAS_V = 0.1  # porcentagem da largura da tela
    linhas_verticais = []

    # Definir as linhas horizontais
    NUM_LINHAS_H = 15
    ESPACO_LINHAS_H = 0.2  # porcentagem da altura da tela
    linhas_horizontais = []

    def __init__(self, **kwargs):
        super(WidgetPrincipal, self).__init__(**kwargs)
        self.init_linhas_verticais()
        self.init_linhas_horizontais()

    # Criar uma função para juntar a tela da aplicação com a tela do widget
    def on_parent(self, widget, parent):
        pass

    # Criar uma função para pegar o tamanho da tela da aplicação
    def on_size(self, *args):
        # Devemos chamar a função que atualiza as linhas
        # Se chamarmos a que inicia, o Kivy cria linhas sempre que a tela é redimezionada
        self.atualizar_linhas_verticais()
        self.atualizar_linhas_horizontais()

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
        offset = -int(self.NUM_LINHAS_V / 2) + 0.5

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_V):
            linha_x = int(linha_central_x + offset * espacamento)

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
        offset = -int(self.NUM_LINHAS_V / 2) + 0.5
        x_min = linha_central_x + offset * espacamento
        x_max = linha_central_x - offset * espacamento
        espacamento_y = self.ESPACO_LINHAS_H * self.height

        # Informar a posição das linhas na tela
        for i in range(0, self.NUM_LINHAS_H):
            linha_y = i * espacamento_y

            # Transformar as linhas
            x1, y1 = self.transformar(x_min, linha_y)
            x2, y2 = self.transformar(x_max, linha_y)

            self.linhas_horizontais[i].points = [x1, y1, x2, y2]

    # Função para transformar as linhas paralelas em transversais
    # Elas se encontram em "ponto_perspectiva_x" e "ponto_perspectiva_y"
    def transformar(self, x, y):
        return self.transformar_perspectiva(x, y)

    # Função para transformar de 2D em 3D (perspectiva)
    def transformar_2D(self, x, y):
        return int(x), int(y)

    # Função para colocar os pontos das linhas nos pontos de perspectiva
    def transformar_perspectiva(self, x, y):
        # Obter o ponto no eixo Y em perspectiva
        tr_y = y * self.ponto_perspectiva_y / self.height

        # Isso evita que a reta passe do ponto de perspectiva
        if tr_y > self.ponto_perspectiva_y:
            tr_y = self.ponto_perspectiva_y

        # Determinar a diferença no eixo X e Y das linhas para que todas
        # possuam uma angulação para chegarem a mesmo ponto de perspectiva
        dif_x = x - self.ponto_perspectiva_x
        dif_y = self.ponto_perspectiva_y - tr_y

        # Determinar a proporção das linhas no eixo Y para que possuam
        # um gradiente de aproximação igual entre todas até o ponto de perspectiva
        proporcao_y = dif_y / self.ponto_perspectiva_y

        # Obter o ponto no eixo X em perspectiva
        tr_x = self.ponto_perspectiva_x + dif_x * proporcao_y

        return int(tr_x), int(tr_y)


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    GalaxyApp().run()
