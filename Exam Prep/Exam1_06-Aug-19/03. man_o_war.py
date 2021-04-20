END_COMMAND = "Retire"
has_winner = False

def is_valid(index, range):
    return index in range

def check_section_health(section):
    return section <= 0

def attack_warship(ship, index, damage):
    global has_winner

    if is_valid(index, range(len(ship))):
        ship[index] -= damage
        attack_result = check_section_health(ship[index])

        if attack_result:
            has_winner = True
            print("You won! The enemy ship has sunken.")

def attack_pirate_ship(ship, start_i, end_i, damage):
    global has_winner

    if is_valid(start_i, range(len(ship))) and is_valid(end_i, range(len(ship))):
        for i in range(start_i, end_i + 1):
            ship[i] -= damage
            attack_result = check_section_health(ship[i])

            if attack_result:
                has_winner = True
                print("You lost! The pirate ship has sunken.")
                break

def increase_section_health(ship, index, health):
    ship[index] += health
    if ship[index] > max_health:
        ship[index] = max_health

def repair_ship(ship, index, health):
    if is_valid(index, range(len(ship))):
        increase_section_health(ship, index, health)

def get_count_of_sections_which_need_repair(pirate_ship):
    counter = 0
    repair_threshold = max_health * 0.2

    for section in pirate_ship:

        if section < repair_threshold:
            counter += 1

    return counter

def execute_commands(commands, pirate_ship, warship):

    for command in commands:

        if command.startswith("Fire"):
            index = int(command.split()[1])
            damage = int(command.split()[2])
            attack_warship(warship, index, damage)

        elif command.startswith("Defend"):
            start_index = int(command.split()[1])
            end_index = int(command.split()[2])
            damage = int(command.split()[3])
            attack_pirate_ship(pirate_ship, start_index, end_index, damage)

        elif command.startswith("Repair"):
            index = int(command.split()[1])
            health = int(command.split()[2])
            repair_ship(pirate_ship, index, health)

        else:
            sections_count = get_count_of_sections_which_need_repair(pirate_ship)
            print(f"{sections_count} sections need repair.")

        if has_winner:
            break

def read_commands():
    result = []

    while True:
        command = input()

        if command == END_COMMAND:
            break
        result.append(command)

    return result

def print_result(pirate_ship, warship):
    if not has_winner:
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship)}")

pirate_ship = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
max_health = int(input())

commands = read_commands()
execute_commands(commands, pirate_ship, warship)
print_result(pirate_ship, warship)