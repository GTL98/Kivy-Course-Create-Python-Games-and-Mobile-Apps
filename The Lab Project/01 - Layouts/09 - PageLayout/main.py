from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout


class ExemploBoxLayout(BoxLayout):
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configurar a orientação da tela
        self.orientation = 'vertical'

        # Criar os botões
        b1 = Button(text='A')
        b2 = Button(text='B')
        b3 = Button(text='C')

        # Adicionar os botões na tela
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
    pass


class ExemploAnchorLayout(AnchorLayout):
    pass


class ExemploStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            #dimensao = dp(100) + i*10
            dimensao = dp(100)
            b = Button(text=str(i+1),
                       size_hint=(None, None),
                       size=(dimensao, dimensao))
            self.add_widget(b)


class MainWidget(Widget):
    pass


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
