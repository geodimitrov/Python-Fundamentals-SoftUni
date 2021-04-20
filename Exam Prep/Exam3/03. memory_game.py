
def read_moves():
    result = []

    while True:
        line = input()

        if line == "end":
            break
        result.append(line)

    return result

def in_range(elements, i_one, i_two):
    return i_one in range(len(elements)) \
        and i_two in range(len(elements))

def valid_indices(elements, i_one, i_two):
    if not i_one == i_two and in_range(elements, i_one, i_two):
        return True

def print_result(elements):
    if elements:
        print(f"Sorry you lose :(\n{' '.join(elements)}")

elements = input().split()
moves = read_moves()
moves_counter = 0

for move in moves:
    index_one = int(move.split()[0])
    index_two = int(move.split()[1])
    moves_counter += 1


    if not valid_indices(elements, index_one, index_two):
        additional_el = f"-{moves_counter}a"
        seq_half = len(elements) // 2
        elements.insert(seq_half, additional_el)
        elements.insert(seq_half, additional_el)
        print("Invalid input! Adding additional elements to the board")

    else:
        element_one = elements[index_one]
        element_two = elements[index_two]

        if not element_one == element_two:
            print("Try again!")

        else:
            elements.remove(element_one)
            elements.remove(element_two)
            print(f"Congrats! You have found matching elements - {element_one}!")

    if not elements:
        print(f"You have won in {moves_counter} turns!")
        break

print_result(elements)