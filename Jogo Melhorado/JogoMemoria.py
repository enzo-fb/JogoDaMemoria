from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import random
from colorama import Fore, Back

def verificacao_cartas(valor, contador):
    if valor < 0 or valor > contador - 1:
        return False
    return True

class JogoMemoria(App):
    def build(self):
        self.cartas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"] * 2
        random.shuffle(self.cartas)
        
        self.botoes = []
        self.reveladas = []
        self.cartas_restantes = len(self.cartas) // 2
        
        layout = GridLayout(cols=4, spacing=10, padding=20)
        for i in range(len(self.cartas)):
            botao = Button(text="?", font_size=24, on_press=self.revelar_carta)
            botao.index = i
            self.botoes.append(botao)
            layout.add_widget(botao)
        
        return layout
    
    def revelar_carta(self, instance):
        index = instance.index
        if instance.text == "?":
            instance.text = self.cartas[index]
            self.reveladas.append(instance)
        
            if len(self.reveladas) == 2:
                Clock.schedule_once(self.verificar_pares, 1)
    
    def verificar_pares(self, dt):
        carta1 = self.reveladas[0]
        carta2 = self.reveladas[1]
        
        if carta1.text == carta2.text:
            print("Cartas iguais!")
            self.cartas_restantes -= 1
            if self.cartas_restantes == 0:
                self.fim_de_jogo("Você ganhou!")
        else:
            print("Cartas diferentes!")
            carta1.text = "?"
            carta2.text = "?"
        
        self.reveladas = []
    
    def fim_de_jogo(self, mensagem):
        print(mensagem)
        Clock.schedule_once(self.restart_game, 3)
    
    def restart_game(self, dt):
        self.cartas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"] * 2
        random.shuffle(self.cartas)
        
        for botao in self.botoes:
            botao.text = "?"
        
        self.reveladas = []
        self.cartas_restantes = len(self.cartas) // 2
        print("Jogo reiniciado!")
        self.layout.clear_widgets()
        self.build()

if __name__ == "__main__":
    JogoMemoria().run()
