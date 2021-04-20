END_COMMAND = "Yohoho!"

def is_valid(index, range):
    return index in range

def remove_items(chest, count):
    if count >= len(chest):
        result = ', '.join(chest)
        chest.clear()
    else:
        result = ', '.join(chest[len(chest) - count:])
        for i in range(count):
            chest.pop()

    print(result)
    return chest

def execute_command(command, chest):

    if command.startswith("Loot"):
        items = command.split()[1:]

        for item in items:
            if item not in chest:
                chest.insert(0, item)

    elif command.startswith("Drop"):
        index = int(command.split()[1])

        if is_valid(index, range(len(chest))):
            chest.append(chest.pop(index))
    else:
        count = int(command.split()[1])
        remove_items(chest, count)


def treasure_hunt(initial_loot):
    treasure_chest = initial_loot

    while True:
        command = input()

        if command == END_COMMAND:
            break

        execute_command(command, treasure_chest)

    return treasure_chest

def print_result(result):

    if not result:
        print("Failed treasure hunt.")
    else:
        average_gain = sum(len(el) for el in result) / len(result)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

initial_loot = input().split("|")
hunt_result = treasure_hunt(initial_loot)
print_result(hunt_result)