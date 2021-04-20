END_COMMAND = "Exhibition"
ERROR = "error"

def read_input_data(n):
    result = {}

    for _ in range(n):
        plant_name, rarity = input().split("<->")

        if plant_name not in result:
            result[plant_name] = {"Rarity": int(rarity), "Ratings": []}

        else:

            if rarity > result[plant_name]:
                result[plant_name]["Rarity"] = int(rarity)

    return result

def execute_commands(plants):

    while True:
        command = input()

        if command == END_COMMAND:
            break

        try:
            command_type, command_data = command.split(": ")

            if command_type == "Rate":
                plant, rating = command_data.split(" - ")
                plants[plant]["Ratings"].append(int(rating))

            elif command_type == "Update":
                plant, new_rarity = command_data.split(" - ")
                plants[plant]["Rarity"] = int(new_rarity)

            elif command_type == "Reset":
                plant = command_data
                plants[plant]["Ratings"].clear()

        except:
            print(ERROR)

def calc_average_ratings(plants):

    for plant in plants:
        rarity = plants[plant]["Rarity"]
        ratings = plants[plant]["Ratings"]

        if ratings:
            average_score = sum(ratings) / len(ratings)
        else:
            average_score = 0

        plants[plant] = [rarity, average_score]


def print_plants(plants):
    sorted_plants = dict(sorted(plants.items(), key=lambda x: x[1], reverse=True))
    print("Plants for the exhibition:")
    for plant, values in sorted_plants.items():
        print(f"- {plant}; Rarity: {values[0]}; Rating: {values[1]:.2f}")

n = int(input())
plants = read_input_data(n)
execute_commands(plants)
calc_average_ratings(plants)
print_plants(plants)