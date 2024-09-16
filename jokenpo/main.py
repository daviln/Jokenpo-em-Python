from tkinter import Tk, Toplevel, Label, Button, Frame
from emoji import emojize
from random import choice

player = 0
draw = 0
bot = 0

root = Tk()
root.title("Davi's Jokenpo Game")
root.geometry('500x300')
root.configure(bg='lightblue')


def computador_escolhe():
    itens = ['pedra', 'papel', 'tesoura']
    item_computador = choice(itens)
    return item_computador

def vencedor(jogador, item_computador):
    global player
    global draw
    global bot
    if jogador == item_computador:
        draw += 1
        return 'DRAW!'
    elif (jogador == 'pedra' and item_computador == 'tesoura') or \
         (jogador == 'papel' and item_computador == 'pedra') or \
         (jogador == 'tesoura' and item_computador == 'papel'):
        player += 1
        return 'YOU WIN!'
    
    else:
        bot += 1
        return 'YOU LOOSE!'

def player_win():
    win_count.config(text=f'Player: {player}')

def draw_win():
    draw_count.config(text=f'Draw: {draw}')

def bot_win():
    bot_count.config(text=f'Bot: {bot}')

def win_loose_window(jogador, item_computador, resultado):
    win_loose = Toplevel(root)
    win_loose.title('Results')
    win_loose.geometry('500x300')
    if jogador == item_computador:
        win_loose.configure(bg='lightblue')
        bg_color='lightblue'
        draw_win()

    elif (jogador == 'pedra' and item_computador == 'tesoura') or \
         (jogador == 'papel' and item_computador == 'pedra') or \
         (jogador == 'tesoura' and item_computador == 'papel'):
         win_loose.configure(bg='green')
         bg_color = 'green'
         player_win()

    else:
        win_loose.configure(bg='red')
        bg_color = 'red'
        bot_win()

    jogador_text = emojize(emoji_map[jogador])
    computador_text = emojize(emoji_map[item_computador])

    Label(win_loose, text=computador_text, font=('', 50), bg=bg_color).pack(pady=10) 
    Label(win_loose, text=resultado, font=('', 30), bg=bg_color).pack(pady=10)
    Label(win_loose, text=jogador_text, font=('', 50), bg=bg_color).pack(pady=10) 

    def play_again():
        win_loose.destroy()
    Button(win_loose, text='Play again', font=('', 20), bg=bg_color, 
           activebackground=bg_color, bd=0, highlightthickness=0, relief='flat', command=play_again).pack(pady=10)

def jogador_escolhe(itens):
    jogador = itens
    item_computador = computador_escolhe()
    resultado = vencedor(jogador, item_computador)
    win_loose_window(jogador, item_computador, resultado)

emoji_map = {
    'pedra':emojize(':oncoming_fist:'),
    'papel':emojize(':hand_with_fingers_splayed:'),
    'tesoura':emojize(':victory_hand:')
}
      
jogo_text = ('Pedra, papel ou tesoura?')
font_jogo = ('Helvetica', 30)
jogo = Label(root, text=jogo_text, font=font_jogo, bg='lightblue', fg='black').pack(pady=10)

computer_text = emojize(':robot:')
font_computer = ('', 50)
computer = Label(root, text=computer_text, font=font_computer, bg='lightblue').pack(pady=10)              

button_frame = Frame(root, bg='lightblue')
button_frame.pack(pady=20)

pedra_text = emojize(':oncoming_fist:')
font_pedra = ('', 50)
pedra = Button(button_frame, text=pedra_text, font=font_pedra, bg='lightblue',
               activebackground='lightblue', bd=0, highlightthickness=0, relief='flat', command=lambda: jogador_escolhe('pedra'))
pedra.pack(side='left', padx=10)

papel_text = emojize(':hand_with_fingers_splayed:')
font_papel = ('', 50)
papel = Button(button_frame, text=papel_text, font=font_papel, bg='lightblue',
               activebackground='lightblue', bd=0, highlightthickness=0, relief='flat', command=lambda: jogador_escolhe('papel'))
papel.pack(side='left', padx=10)

tesoura_text = emojize(':victory_hand:')
font_tesoura = ('', 50)
tesoura = Button(button_frame, text=tesoura_text, font=font_tesoura, bg='lightblue',
                 activebackground='lightblue', bd=0, highlightthickness=0, relief='flat', command=lambda: jogador_escolhe('tesoura'))
tesoura.pack(side='left', padx=10)

win_count = Label(root, text=f'Player: {player}', font=('', 15), bg='lightblue', fg='black') 
win_count.pack(pady=10)

draw_count = Label(root, text=f'Draw: {draw}', font=('', 15), bg='lightblue', fg='black')
draw_count.pack(pady=10)

bot_count = Label(root, text=f'Bot: {bot}', font=('', 15), bg='lightblue', fg='black')
bot_count.pack(pady=10)

Button(root, text='Close game', font=('',20), command=root.destroy,
       activebackground='lightblue', bd=0, highlightthickness=0, relief='flat').pack(pady=10)

root.mainloop()

