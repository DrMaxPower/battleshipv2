import random
row_a = {1: '*', 2: '*', 3: '*', 4: '*'}
row_b = {1: '*', 2: '*', 3: '*', 4: '*'}
row_c = {1: '*', 2: '*', 3: '*', 4: '*'}
row_d = {1: '*', 2: '*', 3: '*', 4: '*'}

# Place Player Ship
list_rows_a_d = [row_a, row_b, row_c, row_d]


computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
print(computer_shoot)
if computer_shoot == 'o':
    computer_shoot = 'x'
elif computer_shoot == 'x':
    computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
elif computer_shoot == 'm':
    computer_shoot = list_rows_a_d[random.randint(0, 3)][random.randint(1, 4)]
elif computer_shoot == '*':
    computer_shoot = 'm'
print(computer_shoot)
