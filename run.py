""" BATTLESHIP """
import random
# all input data needs to be in a new row
# on Heroku: key = PORT, value = 8000


def input_player_ship():
    """ select what key in dict Player wahts to use """
    p = {
        'A': {1: '*', 2: '*', 3: '*', 4: '*'},
        'B': {1: '*', 2: '*', 3: '*', 4: '*'},
        'C': {1: '*', 2: '*', 3: '*', 4: '*'},
        'D': {1: '*', 2: '*', 3: '*', 4: '*'}
    }
    
    # First Ship Position
    first_ship_letter = input("typ letter A - D\n").upper()      
    while (len(first_ship_letter) != 1) or (first_ship_letter not in 'ABCD'):
        print("Not valid data, set your first letter.")
        first_ship_letter = input("typ letter A - D\n").upper()
        
    first_ship_int = input("typ a int 1 - 4\n")

    while (len(first_ship_int) != 1) or (first_ship_int not in '1234'):
        print("Not valid data, set your first int.")
        first_ship_int = input("typ int 1 - 4\n")

    first_ship_int = int(first_ship_int)

    if p[first_ship_letter][first_ship_int] == 'o':
        first_ship_letter = input("typ letter A - D\n").upper()
        first_ship_int = int(input("typ a int 1 - 4\n"))
    else:
        p[first_ship_letter][first_ship_int] = 'o'

    print(f"Your position is:\n {first_ship_letter} {first_ship_int}")

    # Second Ship Position
    second_ship_letter = input("typ letter A - D\n").upper()      
    while (len(second_ship_letter) != 1) or (second_ship_letter not in 'ABCD'):
        print("Not valid data, set your second letter.")
        second_ship_letter = input("typ letter A - D\n").upper()
        
    second_ship_int = input("typ a int 1 - 4\n")

    while (len(second_ship_int) != 1) or (second_ship_int not in '1234'):
        print("Not valid data, set your second int.")
        second_ship_int = input("typ int 1 - 4\n")

    second_ship_int = int(second_ship_int)

    if p[second_ship_letter][second_ship_int] == 'o':
        second_ship_letter = input("typ letter A - D\n").upper()
        second_ship_int = int(input("typ a int 1 - 4\n"))
    else:
        p[second_ship_letter][second_ship_int] = 'o'

    print(f"Your position is:\n {first_ship_letter}{first_ship_int} \
         {second_ship_letter} {second_ship_int}")

    # third Ship Position
    third_ship_letter = input("typ letter A - D\n").upper()      
    while (len(third_ship_letter) != 1) or (third_ship_letter not in 'ABCD'):
        print("Not valid data, set your third letter.")
        third_ship_letter = input("typ letter A - D\n").upper()
        
    third_ship_int = input("typ a int 1 - 4\n")

    while (len(third_ship_int) != 1) or (third_ship_int not in '1234'):
        print("Not valid data, set your third int.")
        third_ship_int = input("typ int 1 - 4\n")

    third_ship_int = int(third_ship_int)

    if p[third_ship_letter][third_ship_int] == 'o':
        third_ship_letter = input("typ letter A - D\n").upper()
        third_ship_int = int(input("typ a int 1 - 4\n"))
    else:
        p[third_ship_letter][third_ship_int] = 'o'

    return p


def place_ship_computer():
    """ """
    computer_dict = {
        'E': {1: '*', 2: '*', 3: '*', 4: '*'},
        'F': {1: '*', 2: '*', 3: '*', 4: '*'},
        'G': {1: '*', 2: '*', 3: '*', 4: '*'},
        'H': {1: '*', 2: '*', 3: '*', 4: '*'}
    }
    for i in range(3):
        letter_row = chr(random.randint(69, 72))
        int_column = random.randint(1, 4)

        while computer_dict[letter_row][int_column] == 'o':
            letter_row = chr(random.randint(69, 72))
            int_column = random.randint(1, 4)
        computer_dict[letter_row][int_column] = 'o'

    print(computer_dict)
    return computer_dict


def player_shoot():
    """ """
    # turns = 5
    # input place_ship_computer dictonary
    # input frpm player where to shoot
    # import player_score 

    print("Your turn to shoot")
    print("Enter where you think enemys at.")
    shot_letter = input("typ letter A - D\n").upper()      
    while (len(shot_letter) != 1) or (shot_letter not in 'ABCD'):
        print("Not valid data, set your first letter.")
        shot_letter = input("typ letter A - D\n").upper()
        
    shot_column = input("typ a int 1 - 4\n")

    while (len(shot_column) != 1) or (shot_column not in '1234'):
        print("Not valid data, set your first int.")
        shot_column = input("typ int 1 - 4\n")

    shot_column = int(shot_column)


    # chage COMPUTERBOARD to valid dict from computer board 
    # FIX BETTER THEN xx etc a list of shot_letter and shot_column
    if COMPUTERBOARD[shot_letter][shot_column] == 'xx':
        print("You have sunk an shit there already")
        shot_letter = input("typ letter A - D\n").upper()
        shot_column = int(input("typ a int 1 - 4\n"))

    # chage COMPUTERBOARD to valid dict from computer board
    elif COMPUTERBOARD[shot_letter][shot_column] == 'm':
        print("You have already tried to shoot there")
        shot_letter = input("typ letter A - D\n").upper()
        shot_column = int(input("typ a int 1 - 4\n"))
    
    elif COMPUTERBOARD[shot_letter][shot_column] == 'x':
        print(" You hit an enemy ship ")
        player_score += 1



    # return hit, player_score or miss to board_ternminal
    

def computers_tur_to_shoot():
    """ """
    # import player_ship_dict
    # import computer_score 
    computer_int_letter_shot = random.randint(69, 72)
    computer_letter_shot = chr(computer_int_letter_shot)
    computer_int_shot = random.randint(1, 4)

    if player_ship_dict[computer_letter_shot][computer_int_shot] == 'xx':
        computer_int_letter_shot = random.randint(69, 72)
        computer_int_shot = random.randint(1, 4)
    
    elif player_ship_dict[computer_letter_shot][computer_int_shot] == 'm':
        computer_int_letter_shot = random.randint(69, 72)
        computer_int_shot = random.randint(1, 4)

    elif player_ship_dict[computer_letter_shot][computer_int_shot] == 'x':
        computer_score += 1

        
def score():
    """ seting score for player and computer """

    # c = computer dict board with ships on
    player_score = 0
    for j in range(4):
        letter_computer = chr(69+j)
        hit_computer = (c.get(letter_computer).values())
        for item in hit_computer:
            if item == 'x':
                player_score += 1

    # p = player dict board with ships on
    computer_score = 0
    for i in range(4):
        letter_player = chr(65+i)
        hit_player = (p.get(letter_player).values())
        for item in hit_player:
            if item == 'x':
                computer_score += 1

    return player_score, computer_score


def board_ternminal():
    """"""
    tunrs = 3

    wall = '|'
    roof = '-=-'
    mine = '¤ '

    print(" "*20)
    # print("PLAYER", " "*3, f"SCORE: {player_score}")
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
    # print("COMPUTER", " ", f"SCORE: {computer_score}")
    print(" "*20)


def main():
    pass