""" BatleShip """
import random
import re
from collections import Counter





def player_board():
    """
    playerboard is made of four dictionary
    * input  where to put ship
    * input where computer shoot
    """
    # Players water
    row_a = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_b = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_c = {1: '*', 2: '*', 3: '*', 4: '*'}
    row_d = {1: '*', 2: '*', 3: '*', 4: '*'}

    # Place Player Ship
    # list_rows_a_d = [row_a, row_b, row_c, row_d]
    # letters_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    print("Type where you like to place ship:")
    print("Example: A3 or C4 ")
    input_player = input("where to place ship:\n")

    r = re.compile("([a-dA-D]+)([1-4]+)")
    m = r.match(input_player)
    m.group(1).upper()
    print(type(int(m.group(2))))


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

    return score_computer


player_board()