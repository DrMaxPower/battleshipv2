""" BATTLEFIELD """
import random
# all input data needs to be in a new row
# on Heroku: key = PORT, value = 8000


def input_player():
    pass


def validate_input_player():
    pass


def place_ship_computer():
    pass

def place_ship_player():
    pass


def player_shoot():
    pass


def board():
    """ player and compter board """

    # Players Board
    p = {
        'A': {1: 'x', 2: '*', 3: '*', 4: '*'},
        'B': {1: '*', 2: '*', 3: 'x', 4: '*'},
        'C': {1: '*', 2: '*', 3: '*', 4: '*'},
        'D': {1: 'x', 2: 'o', 3: '*', 4: '*'}
    }

    # Computers Board
    c = {
        'E': {1: 'x', 2: '*', 3: '*', 4: '*'},
        'F': {1: '*', 2: '*', 3: '*', 4: '*'},
        'G': {1: '*', 2: 'x', 3: '*', 4: '*'},
        'H': {1: '*', 2: '*', 3: 'x', 4: '*'}
    }

    return p, c


def score():
    """ seting score for player and computer """

    player_score = 0
    for j in range(4):
        letter_computer = chr(69+j)
        hit_computer = (c.get(letter_computer).values())
        for item in hit_computer:
            if item == 'x':
                player_score += 1

    computer_score = 0
    for i in range(4):
        letter_player = chr(65+i)
        hit_player = (p.get(letter_player).values())
        for item in hit_player:
            if item == 'x':
                computer_score += 1

    return player_score, computer_score


def board_ternminal(p, c, player_score, computer_score):
    """"""
    tunrs = 3

    wall = '|'
    roof = '-=-'
    mine = '¤ '

    print(" "*20)
    print("PLAYER", " "*3, f"SCORE: {player_score}")
    print('   ', '1', '2', '3', '4')
    print('+', roof*3, '+')
    print('A', wall, p['A'][1], p['A'][2], p['A'][3], p['A'][4], wall, " * : water ")
    print('B', wall, p['B'][1], p['B'][2], p['B'][3], p['B'][4], wall, " o : ship")
    print('C', wall, p['C'][1], p['C'][2], p['C'][3], p['C'][4], wall, " x : hit")
    print('D', wall, p['D'][1], p['D'][2], p['D'][3], p['D'][4], wall)

    print('  +', mine*4)
    print(f"  Turn: {tunrs}")
    print('  +', mine*4)

    print('E', wall, c['E'][1], c['E'][2], c['E'][3], c['E'][4], wall, " 1 : Position your ship")
    print('F', wall, c['F'][1], c['F'][2], c['F'][3], c['F'][4], wall, " 2 : Enter your shoot")
    print('G', wall, c['G'][1], c['G'][2], c['G'][3], c['G'][4], wall)
    print('H', wall, c['H'][1], c['H'][2], c['H'][3], c['H'][4], wall)
    print('+', roof*3, '+')
    print('  ', '1', '2',  '3', '4')
    print("COMPUTER", " ", f"SCORE: {computer_score}")
    print(" "*20)


def main():
    pass