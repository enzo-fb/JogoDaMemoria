from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random

class JogoMemoria(App):
    def build(self):
        self.cartas = ["A","B","C","D","E","F","G","H","I","J","K","L"] * 2
        random.shuffle(self.cartas)
        self.botoes = []
        
        layout = GridLayout(cols=4, spacing=10, padding=20)
        for i in range(len(self.cartas)):
            botao = Button(text="?", font_size=24, on_press=self.revelar_carta)
            botao.index = i  # Armazena o índice da carta
            self.botoes.append(botao)
            layout.add_widget(botao)
        
        return layout
    
    def revelar_carta(self, instance):
        index = instance.index
        instance.text = self.cartas[index]
        
JogoMemoria().run()
