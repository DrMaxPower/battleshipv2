""" BatleShip """
import random
import re
import os
from collections import Counter





def player_board():
    """
    playerboard is made of four dictionary
    * input  where to put ship
    * input where computer shoot
    """

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
    print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, " * : water")
    print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, " o : ship")
    print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, " x : hit")
    print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)

    ship_counts = 0

    while ship_counts < 3:
        input_player = input("where to place ship.\nExample: A3 or C4\n")

        r = re.compile("([a-dA-D]+)([1-4]+)")
        m = r.match(input_player)
        ship_row = m.group(1).upper()
        ship_col = int(m.group(2))

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
        print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, " * : water ")
        print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, " o : ship")
        print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, " x : hit")
        print('D', wall, row_d[1], row_d[2], row_d[3], row_d[4], wall)
        if ship_counts == 3:
            os.system('clear')
            print("lets start the game")


    # computer playground
    row_a_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_b_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_c_comp = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_d_comp = {1: '*', 2: '*', 3: '*', 4: '*'}


    # score_computer
    counter_row_a = Counter(row_a.values())
    hit_on_row_a = counter_row_a['x']

    counter_row_b = Counter(row_b.values())
    hit_on_row_b = counter_row_b['x']

    counter_row_c = Counter(row_c.values())
    hit_on_row_c = counter_row_c['x']

    counter_row_d = Counter(row_d.values())
    hit_on_row_d = counter_row_d['x']

    score_computer = sum(

        [hit_on_row_a, hit_on_row_b, hit_on_row_c, hit_on_row_d]

        )

    # GameBoard
    print(" "*20)
    print('   ', '1', '2', '3', '4')
    print('+', roof*3, '+')
    print('A', wall, row_a[1], row_a[2], row_a[3], row_a[4], wall, " * : water")
    print('B', wall, row_b[1], row_b[2], row_b[3], row_b[4], wall, " o : ship")
    print('C', wall, row_c[1], row_c[2], row_c[3], row_c[4], wall, " x : hit")
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
    # print("COMPUTER", " ", f"SCORE: {computer_score}")
    print(" "*20)


player_board()