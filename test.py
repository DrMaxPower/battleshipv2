# computer playground not shown
import random
from collections import Counter

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

        [comp_ship_on_row_a, comp_ship_on_row_b, comp_ship_on_row_c, comp_ship_on_row_d]

    )
