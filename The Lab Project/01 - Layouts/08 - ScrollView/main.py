from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


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


class LabApp(App):
    pass


if __name__ == '__main__':
    LabApp().run()
