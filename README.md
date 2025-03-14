# Jogo da Memória

O **Jogo da Memória** é um jogo simples onde o jogador deve encontrar pares de cartas iguais. O jogo é jogado no terminal, e o objetivo é combinar as cartas corretamente o mais rápido possível.

## Como Jogar

1. O jogo apresenta duas listas de cartas embaralhadas (cartas1 e cartas2).
2. O jogador escolhe duas posições de cartas para virar e verificar se são iguais.
3. Se as cartas forem iguais, elas são removidas do jogo. Caso contrário, o jogador deve tentar novamente.
4. O objetivo é formar todos os pares de cartas.

### Regras

- O jogador deve escolher as posições das cartas usando números entre 0 e 11.
- O jogo exibe as cartas embaralhadas e permite ao jogador tentar formar os pares.
- Quando o jogador acerta um par, as cartas são removidas e o número de cartas disponíveis diminui.
- O jogo termina quando todos os pares são encontrados.

## Tecnologias Usadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento.
- **Colorama**: Biblioteca usada para melhorar a aparência das cores no terminal.

## Como Executar o Jogo

Para rodar o jogo em seu computador, siga as instruções abaixo:

### 1. Clonar o Repositório

```bash
git clone https://github.com/enzo-fb/JogoDaMemoria
```
2. Instalar Dependências
<p>O jogo utiliza a biblioteca colorama para colorir o texto no terminal. Para instalá-la, execute:</p>

```bash
pip install colorama
```
3. Rodar o Jogo
<p> Abra o terminal na pasta do projeto e execute o script:</p>

```bash
python3 main.py
```
4. Iniciar o Jogo
Siga as instruções no terminal para começar a jogar.

Como Funciona
1. O jogo começa com um embaralhamento das cartas.
1. O jogador escolhe duas cartas de diferentes listas de cartas para combinar.
1. Se as cartas forem iguais, elas são removidas. Se forem diferentes, o jogo continua.
1. Quando todas as cartas forem removidas, o jogo termina.
```
Bem-vindo ao jogo da memória!
Vamos começar!
Cartas disponíveis:
[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11]
['F', 'J', 'E', 'A', 'B', 'I', 'D', 'H', 'C', 'G', 'K', 'L']
['J', 'G', 'D', 'H', 'A', 'I', 'K', 'F', 'L', 'B', 'C', 'E']

Escolha a posição da carta (0 a 11)
Digite a posição primeira carta:
0
Escolha a posição da carta (0 a 11)
Digite a posição segunda carta:
1
Cartas diferentes!
...

Fim de jogo!
Deseja jogar novamente?
Digite 'sim' para jogar novamente ou 'não' para sair:
```
