# will use multidimensional lists (matrices) to solve the problem
# use a func to create the field
def create_field(n):
    result = []
    for line in range(n):
        result.append([int(el) for el in input().split()]) # turn elements into ints
    return result

def is_ship(field, row, col):
    if field[row][col] > 0:
        return True

def attack_cell(field, row, col, destroyed_ships):
    if field[row][col] > 1:
        field[row][col] -= 1
    else:
        field[row][col] = 0
        destroyed_ships += 1
    return destroyed_ships

def execute_attacks(attacks_info, field):
    destroyed_ships = 0

    for attack in attacks_info:
        row = int(attack[0])
        column = int(attack[2])
        if is_ship(field, row, column):
            destroyed_ships = attack_cell(field, row, column, destroyed_ships)

    return destroyed_ships

n = int(input())
field = create_field(n)
attacks = input().split()
ships_destroyed = execute_attacks(attacks, field)
print(ships_destroyed)