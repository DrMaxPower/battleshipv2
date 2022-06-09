""" BATTLEFIELD """
import random

# all input data needs to be in a new row
# on Heroku: key = PORT, value = 8000

# NAME = input("What is your GamePlay Name_:")




# Players Board
A = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
B = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
C = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
D = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}



# Computers Board
E = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
F = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
G = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}
H = {1: '* ', 2: ' * ', 3: ' * ', 4: ' *'}


def board():
    """"""
    player_score = 7
    computer_score = 4
    tunrs = 3

    wall = '|'
    roof = '-=-'
    mine = '¤ '

    print(" "*20)
    print("PLAYER", " "*3, f"SCORE: {player_score}")
    print(' ', '  1', '  2',  '  3', '  4')
    print('+', roof*5, '+')
    print('A', wall, A[1], A[2], A[3], A[4], wall)
    print('B', wall, B[1], B[2], B[3], B[4], wall)
    print('C', wall, C[1], C[2], C[3], C[4], wall)
    print('D', wall, D[1], D[2], D[3], D[4], wall)

    print('  +', mine*7, '+')
    print(' ', wall, f"Turns left: {tunrs}", wall)
    print('  +', mine*6, '+')

    print('E', wall, E[1], E[2], E[3], E[4], wall)
    print('F', wall, F[1], F[2], F[3], F[4],  wall)
    print('G', wall, G[1], G[2], G[3], G[4],  wall)
    print('H', wall, H[1], H[2], H[3], H[4],  wall)
    print('+', roof*5, '+')
    print(' ', '  1', '  2',  '  3', '  4')
    print("COMPUTER", " ", f"SCORE: {computer_score}")
    print(" "*20)


board()