from random import choice


def play():
    user = input("Qual sua escolha?\n 'R' para Rocha, 'T' para Tesoura, 'P' para papel\n").upper()
    computer = choice(['R', 'T', 'P'])

    if user == computer:
        return print("Empate")

    if is_win(user, computer):
        return print("Você Ganhou")
    else:
        return print("Você Perdeu")

def is_win(player, opponent):
    if (player == 'R' and opponent == 'T') or (player == 'T' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True


x = None

while x != 'N':
    play()
    x = input("Quer jogar novamente?\n 'S' sim ou 'N' não\n").upper()
