
def read_towns_data(end_command):
    result = []

    while True:
        line = input()

        if line == end_command:
            break
        result.append(line)

    return result

def process_towns_data(data):
    result = {}

    for el in data:
        town, population, gold = el.split("||")
        if town not in result:
            result[town] = [int(population), int(gold)]
        else:
            result[town][0] += int(population)
            result[town][1] += int(gold)

    return result

def read_and_store_events(end_command):
    result = []

    while True:
        event = input()

        if event == end_command:
            break

        result.append(event)

    return result

def check_town_population_and_gold(towns, town_name):
    population = towns[town_name][0]
    gold = towns[town_name][1]

    if population == 0 or gold == 0:
        print(f"{town_name} has been wiped off the map!")
        del towns[town_name]

def plunder_town(towns, town_name, people, gold):
    towns[town_name][0] -= people
    towns[town_name][1] -= gold
    print(f"{town_name} plundered! {gold} gold stolen, {people} citizens killed.")
    check_town_population_and_gold(towns, town_name)

def is_valid_amount(value):
    return value >= 0

def add_prosperity_to_town(towns, town_name, gold):
    if not is_valid_amount(gold):
        print("Gold added cannot be a negative number!")
        return

    towns[town_name][1] += gold
    print(f"{gold} gold added to the city treasury. "
          f"{town_name} now has {towns[town_name][1]} gold.")

def execute_command(event, towns):

    if event.startswith("Plunder"):
        town, people, gold = event.split("=>")[1:]
        plunder_town(towns, town, int(people), int(gold))

    else:
        town, gold = event.split("=>")[1:]
        add_prosperity_to_town(towns, town, int(gold))

def print_result(towns):
    if towns:
        sorted_towns = dict(sorted(towns.items(), key=lambda x: (-x[1][1], x[0])))
        print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
        for town, values in sorted_towns.items():
            print(f"{town} -> Population: {values[0]} citizens, Gold: {values[1]} kg")

    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")

towns_data = read_towns_data("Sail")
towns = process_towns_data(towns_data)
events = read_and_store_events("End")

for event in events:
    execute_command(event, towns)

print_result(towns)