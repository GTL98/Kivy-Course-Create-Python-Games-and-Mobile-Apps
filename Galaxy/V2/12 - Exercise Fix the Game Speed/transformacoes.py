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
    lin_y = y * self.ponto_perspectiva_y / self.height

    # Isso evita que a reta passe do ponto de perspectiva
    if lin_y > self.ponto_perspectiva_y:
        lin_y = self.ponto_perspectiva_y

    # Determinar a diferença no eixo X e Y das linhas para que todas
    # possuam uma angulação para chegarem a mesmo ponto de perspectiva
    dif_x = x - self.ponto_perspectiva_x
    dif_y = self.ponto_perspectiva_y - lin_y

    # Determinar a proporção das linhas no eixo Y para que possuam
    # um gradiente de aproximação igual entre todas até o ponto de perspectiva
    fator_y = dif_y / self.ponto_perspectiva_y
    fator_y = pow(fator_y, 4)

    # Obter o ponto no eixo X em perspectiva
    tr_x = self.ponto_perspectiva_x + dif_x * fator_y

    # Obter o ponto no eixo Y em perspectiva
    tr_y = self.ponto_perspectiva_y - fator_y * self.ponto_perspectiva_y

    return int(tr_x), int(tr_y)
