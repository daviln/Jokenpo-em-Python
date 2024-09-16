# Jokenpo em Python
Um jogo simples de pedra, papel, tesoura em Python

Usando as bibliotecas Tkinter, Emoji e Random, criei um jogo de Pedra Papel e Tesoura em Python, onde você pode jogar contra o computador (bot).

Dando início ao jogo:
Após rodar o código, uma janela Tkinter é aberta, e você pode começar o jogo.
A presença dos emojis gera um visual mais atrativo para o game, com os sinais da mão representando as suas escolhas dentro do jogo (pedra, papel ou tesoura) e o robô o seu adversário, o bot.

Após fazer sua escolha, uma outra janela Tkinter é aberta com o resultado da partida, mostrando a opção do bot, a sua, e uma mensagem de vitória, empate ou derrota.

As mensagens de resultado acompanham uma cor na tela para gerar um visual mais atrativo, sendo:
- 'You win' em verde (vitória do jogador)
- 'You loose' em vermelho (vitória do bot)
- 'Draw' em azul claro (empate)

Na tela de resultados, tem um botão intitulado 'Play Again', onde, ao clicar, você é direcionado novamente para a tela inicial para uma nova partida.

Ao voltar a tela inicial, há uma contagem de pontos, seja para o jogador ('Player'), para o bot ('Bot'), ou para empates ('Draw').

Sempre que uma nova partida é iniciada, há um acumulo de pontos referente ao vencedor da partida anterior. Caso haja empate, um novo ponto é adicionado na contagem 'Draw'.

O jogador pode fechar o jogo quando quiser clicando no botão 'Close game', na janela principal.

Sobre as bibliotecas:
- Tkinter: Usada para criação das janelas para o jogo. Com ela, é possível criar aplicações com interfaces gráficas. A partir dela são criados os botões e comandos do jogo.
- Emoji: Uma biblioteca simples que permite a utilização de emojis dentro do código. Gera uma visual mais atrativo no código, prezando por uma estética 'divertida'.
- Random: Utilizada para randomizar as escolhar do bot dentro do jogo. Dessa forma, durante as rodadas o bot poderá randomizar suas escolhas dentro das opções disponíveis (pedra, papel, tesoura). Uma forma simples de promover um jogo versus contra o computador, de forma justa.

