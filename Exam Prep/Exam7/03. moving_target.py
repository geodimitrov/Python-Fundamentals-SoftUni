END_COMMAND = "End"

def read_commands():
    result = []

    while True:
        command = input()

        if command == END_COMMAND:
            break
        result.append(command)

    return result

def is_valid_index(index, range):
    return index in range

def shoot_target(targets, index, power):
    targets[index] -= power

    if targets[index] <= 0:
        targets.pop(index)

def insert_target(targets, index, value):
    targets.insert(index, value)

def remove_targets_within_range(targets, left_index, right_index):
    for i in range(left_index, right_index + 1):
        targets.remove(targets[left_index])

def execute_command(command, targets):

    if command.startswith("Shoot"):
        index = int(command.split()[1])
        power = int(command.split()[2])

        if is_valid_index(index, range(len(targets))):
            shoot_target(targets, index, power)

    elif command.startswith("Add"):
        index = int(command.split()[1])
        value = int(command.split()[2])

        if not is_valid_index(index, range(len(targets))):
            print("Invalid placement!")

        else:
            insert_target(targets, index, value)

    else:
        index = int(command.split()[1])
        radius = int(command.split()[2])
        left_index = index - radius
        right_index = index + radius

        if is_valid_index(left_index, range(len(targets))) \
                and is_valid_index(right_index, range(len(targets))):
            remove_targets_within_range(targets, left_index, right_index)
        else:
            print("Strike missed!")

targets = [int(el) for el in input().split()]
commands = read_commands()

for command in commands:
    execute_command(command, targets)

print("|".join(str(el) for el in targets))