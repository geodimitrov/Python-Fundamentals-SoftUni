

NULL = "null"


def check_for_nulls(damage, health, armor):
    global NULL

    if damage == NULL:
        damage = 45
    if health == NULL:
        health = 250
    if armor == NULL:
        armor = 10

def add_dragon_features(result, d_type, name, damage, health, armor):
    result[d_type].append("name": name)
    result[d_type].append("damage": damage
    result[d_type]["health"] = health
    result[d_type]["armor"] = armor
    return result


def get_dragons_data(data):
    result = {}
    for el in data:
        d_type, name, damage, health, armor = el.split()
        check_for_nulls(damage, health, armor)
        if d_type not in result:
            result[d_type] = []
        result = add_dragon_features(result, d_type, name, damage, health, armor)
    return result


n = 5
data = ["Red Bazgargal 100 2500 25",
        "Black Dargonax 200 3500 18",
        "Red Obsidion 220 2200 35",
        "Blue Kerizsa 60 2100 20",
        "Blue Algordox 65 1800 50"
        ]

dragons = get_dragons_data(data)
print(dragons)