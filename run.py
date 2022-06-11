""" BatleShip """
import random
import re
import os
from collections import Counter


def play_battle_ship():
    """
    playerboard is made of four dictionary
    * input  where to put ship
    * input where computer shoot
    """
    os.system('clear')
    tunrs = 3
    wall = '|'
    roof = '-=-'
    mine = '¤ '

    # Players water
    row_a = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_b = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_c = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_d = {1: '*', 2: '*', 3: '*', 4: '*'}

    # Place Player Ship
    list_rows_a_d = [row_a, row_b, row_c, row_d]
    letters_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    print('   ', '1', '2', '3', '4')
    print('+', roof*3, '+')
    print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, "* : water")
    print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, "o : ship")
    print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, "x : hit")
    print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)

    ship_counts = 0

    while ship_counts < 3:
        input_player = input(f"where to place ship.\nExample:\
    {random.choice(['A','B','C','D'])}{random.randint(1, 4)} or \
{random.choice(['A','B','C','D'])}{random.randint(1, 4)} \n")

        r = re.compile("([a-dA-D]+)([1-4]+)")
        m = r.match(input_player)
        ship_row = m.group(1).upper()
        ship_col = int(m.group(2))

        # unpack the list number and then dict dict number
        list_rows_a_d[letters_to_int[ship_row]][ship_col] = 'o'

        counter_row_a = Counter(row_a.values())
        ship_on_row_a = counter_row_a['o']

        counter_row_b = Counter(row_b.values())
        ship_on_row_b = counter_row_b['o']

        counter_row_c = Counter(row_c.values())
        ship_on_row_c = counter_row_c['o']

        counter_row_d = Counter(row_d.values())
        ship_on_row_d = counter_row_d['o']

        ship_counts = sum(

        [ship_on_row_a, ship_on_row_b, ship_on_row_c, ship_on_row_d]

        )
        os.system('clear')
        print('   ', '1', '2', '3', '4')
        print('+', roof*3, '+')
        print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, "* : water")
        print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, "o : ship")
        print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, "x : hit")
        print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)
        if ship_counts == 3:
            os.system('clear')
            print("lets start the game")

    # computer playground not shown
    row_a_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_b_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_c_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_d_comp = {1: '*', 2: '*', 3: '*', 4: '*'}

    list_row_comp = [
        row_a_comp,
        row_b_comp,
        row_c_comp,
        row_d_comp,
    ]

    # computer playground not shown
    row_a_comp_hide = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_b_comp_hide = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_c_comp_hide = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_d_comp_hide = {1: '*', 2: '*', 3: '*', 4: '*'}

    list_row_comp_hide = [
        row_a_comp_hide,
        row_b_comp_hide,
        row_c_comp_hide,
        row_d_comp_hide,
    ]

    # Computer Places Ships on Board
    ship_counts_computer = 0
    while ship_counts_computer < 3:
        list_row_comp_hide[random.randint(0, 3)][random.randint(1, 4)] = 'o'

        value_row_a = Counter(row_a_comp_hide.values())
        comp_ship_on_row_a = value_row_a['o']

        value_row_b = Counter(row_b_comp_hide.values())
        comp_ship_on_row_b = value_row_b['o']

        value_row_c = Counter(row_c_comp_hide.values())
        comp_ship_on_row_c = value_row_c['o']

        value_row_d = Counter(row_d_comp_hide.values())
        comp_ship_on_row_d = value_row_d['o']

        ship_counts_computer = sum(
            [
                comp_ship_on_row_a, comp_ship_on_row_b,
                comp_ship_on_row_c, comp_ship_on_row_d
            ]
        )
    
    score_player = 0
    score_computer = 0
    os.system('clear')
    while (score_player < 3) or (score_computer < 3):
        # GameBoard
        print("PLAYER", " ", f"SCORE: {score_player}")
        print(" "*20)
        print('   ', '1', '2', '3', '4')
        print('+', roof*3, '+')
        print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, '* : water')
        print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, "o : ship")
        print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, "x : hit")
        print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)

        print('  +', mine*4)
        print(f"  Turn: {tunrs}")
        print('  +', mine*4)

        print('E', wall, row_a_comp[1], row_a_comp[2], row_a_comp[3], row_a_comp[4], wall, " 1 : Position your ship")
        print('F', wall, row_b_comp[1], row_b_comp[2], row_b_comp[3], row_b_comp[4], wall, " 2 : Enter your shoot")
        print('G', wall, row_c_comp[1], row_c_comp[2], row_c_comp[3], row_c_comp[4], wall)
        print('H', wall, row_d_comp[1], row_d_comp[2], row_d_comp[3], row_d_comp[4], wall)
        print('+', roof*3, '+')
        print('  ', '1', '2',  '3', '4')
        print("COMPUTER", " ", f"SCORE: {score_computer}")
        print(" "*20)

        input_player = input(f"Where to fire.\nExample: \
        {random.choice(['E','F','G','H'])}{random.randint(1, 4)}\n")

        r_f = re.compile("([e-hE-H]+)([1-4]+)")
        m_f = r_f.match(input_player)
        shoot_row = m_f.group(1).upper()
        shoot_col = int(m_f.group(2))

        #  Player shooting at Computer
        comp_letters_to_int = {'E': 0, 'F': 1, 'G': 2, 'H': 3}
        if (list_row_comp_hide[comp_letters_to_int[shoot_row]][shoot_col] == 'o'):
            list_row_comp[comp_letters_to_int[shoot_row]][shoot_col] = 'x'
            score_player += 1
        elif (list_row_comp_hide[comp_letters_to_int[shoot_row]][shoot_col] == '*'):
            list_row_comp[comp_letters_to_int[shoot_row]][shoot_col] = 'm'


        # Computer shooting at Player
        computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
        if computer_shoot == 'o':
            computer_shoot = 'x'
            score_computer += 1
        if computer_shoot == 'x':
            computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
        if computer_shoot == 'm':
            computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
        if computer_shoot == '*':
            computer_shoot = 'm'



        # GameBoard
        os.system('clear')
        print(" "*20)
        print("COMPUTER", " ", f"SCORE: {score_player}")
        print('   ', '1', '2', '3', '4')
        print('+', roof*3, '+')
        print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, '* : water')
        print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, "o : ship")
        print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, "x : hit")
        print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)

        print('  +', mine*4)
        print(f"  Turn: {tunrs}")
        print('  +', mine*4)

        print('E', wall, row_a_comp[1], row_a_comp[2], row_a_comp[3], row_a_comp[4], wall, " 1 : Position your ship")
        print('F', wall, row_b_comp[1], row_b_comp[2], row_b_comp[3], row_b_comp[4], wall, " 2 : Enter your shoot")
        print('G', wall, row_c_comp[1], row_c_comp[2], row_c_comp[3], row_c_comp[4], wall)
        print('H', wall, row_d_comp[1], row_d_comp[2], row_d_comp[3], row_d_comp[4], wall)
        print('+', roof*3, '+')
        print('  ', '1', '2',  '3', '4')
        print("COMPUTER", " ", f"SCORE: {score_computer}")
        print(" "*20)

        os.system('clear')

    # GameBoard
    print(" "*20)
    print("COMPUTER", " ", f"SCORE: {score_player}")
    print('   ', '1', '2', '3', '4')
    print('+', roof*3, '+')
    print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, '* : water')
    print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, "o : ship")
    print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, "x : hit")
    print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)

    print('  +', mine*4)
    print(f"  Turn: {tunrs}")
    print('  +', mine*4)

    print('E', wall, row_a_comp[1], row_a_comp[2], row_a_comp[3], row_a_comp[4], wall, " 1 : Position your ship")
    print('F', wall, row_b_comp[1], row_b_comp[2], row_b_comp[3], row_b_comp[4], wall, " 2 : Enter your shoot")
    print('G', wall, row_c_comp[1], row_c_comp[2], row_c_comp[3], row_c_comp[4], wall)
    print('H', wall, row_d_comp[1], row_d_comp[2], row_d_comp[3], row_d_comp[4], wall)
    print('+', roof*3, '+')
    print('  ', '1', '2',  '3', '4')
    print(" "*20)
    print("COMPUTER", " ", f"SCORE: {score_computer}")
    print(" "*20)


play_battle_ship()