from kivy.uix.relativelayout import RelativeLayout

# Criar a função da captura de teclas para o Kivy
def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


# Criar a função da captura do pressionamento da tecla para o Kivy
def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.velocidade_atual_x = self.VELOCIDADE_X
    elif keycode[1] == 'right':
        self.velocidade_atual_x = -self.VELOCIDADE_X

    return True


# Criar a função da captura da soltura da tecla para o Kivy
def on_keyboard_up(self, keyboard, keycode):
    self.velocidade_atual_x = 0

    return True


# Criar a função que reconhece o toque
def on_touch_down(self, touch):
    if not self.game_over and self.jogo_comecou:
        # Verificar se o toque foi do lado esquerdo da tela
        if touch.x < self.width / 2:
            self.velocidade_atual_x = self.VELOCIDADE_X

        # Verificar se o toque foi do lado direito da tela
        else:
            self.velocidade_atual_x = -self.VELOCIDADE_X

    # Devemos retornar isso aqui embaixo, pois essa função não deixa
    # que o Kivy tenha o comportamento padrão com os botões. Sem isso
    # fica impossível de clicar em qualquer botão
    return super(RelativeLayout, self).on_touch_down(touch)


# Criar a função que reconhece que já não teve mais o toque
def on_touch_up(self, touch):
    self.velocidade_atual_x = 0