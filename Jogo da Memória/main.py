import random
import time
import os
from colorama import Fore, Back, Style
def verificacao_cartas(valor, contador):
    if valor<0 or valor>contador-1:
        print(f"Valor inválido! Digite um valor entre 0 e {contador}: ")
        return False
    else:
        return True
    
    

contagem = ["0","1","2","3", "4","5","6","7","8","9","10","11"]
cartas1 = ["A","B","C","D","E","F","G","H","I","J ","K","L "]
cartas2 = ["A","B","C","D","E","F","G","H","I","J ","K","L "]
while(True):
    print("Bem-vindo ao jogo da memória!".center(50))

    print("Vamos começar!".center(50))
    while(True):
        print("Cartas disponíveis:\n".center(50))
        random.shuffle(cartas1)
        random.shuffle(cartas2)
        print(Back.LIGHTCYAN_EX+Fore.BLACK+str(contagem)+Fore.RESET+Back.RESET)
        print(Back.RED+Fore.WHITE+str(cartas1)+Fore.RESET)
        print(Fore.BLUE+str(cartas2)+Fore.RESET+Back.RESET)
        print(Back.LIGHTCYAN_EX+Fore.BLACK+str(contagem)+Fore.RESET+Back.RESET)
        if len(contagem)>10:
            time.sleep(5)
        elif len(contagem)>5 & len(contagem)<=10:
            time.sleep(3)
        else:
            time.sleep(1)
        os.system('clear')
        while(True):
            print(f"Escolha a posição da carta (0 a {len(cartas1)-1})".center(50))
            try:
                carta1 = int (input("Digite a posição primeira carta: "))
                if verificacao_cartas(carta1, len(cartas1)):
                    break
            except:
                print(Fore.RED +"\nValor inválido! Digite um valor entre 0 e 11".upper().center(50)+Fore.RESET)
        while(True):
            print(f"Escolha a posição da carta (0 a {len(cartas2)-1}):")
            try:
                carta2 = int (input("Digite a posição segunda carta: "))
                if verificacao_cartas(carta2, len(cartas2)):
                    break
            except:
                print(Fore.RED +"\nValor inválido! Digite um valor entre 0 e 11".upper().center(50)+Fore.RESET)           
        if cartas1[carta1] == cartas2[carta2]:
            print("Cartas iguais!")
            cartas1.remove(cartas1[carta1])
            cartas2.remove(cartas2[carta2])
            contagem = contagem[:-1]
        else:
            print("Cartas diferentes!".upper())
        if len(cartas1) == 1:
            print(cartas1) 
            print(cartas2)
            print("\n\nFim de jogo!\n".upper().center(50))
            break
    print("Deseja jogar novamente?")
    jogar_novamente = input("Digite 'sim' para jogar novamente ou 'não' para sair: ")
    if jogar_novamente == 'não' or jogar_novamente == 'nao' or jogar_novamente == 'n':
        print("\n\nObrigado por jogar!".upper().center(50))
        print("Até a próxima!".center(50))
        break