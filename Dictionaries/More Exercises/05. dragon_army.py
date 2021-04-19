class Dragon:
    default_health = 250
    default_damage = 45
    default_armor = 10
    NULL = "null"

    def __init__(self, type, name, damage, health, armor):
        self.type = type
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if value == self.NULL:
            value = self.default_damage
        self.__damage = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value == self.NULL:
            value = self.default_health
        self.__health = value

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        if value == self.NULL:
            value = self.default_armor
        self.__armor = value

class DragonCollector:
    def __init__(self):
        self.repository = {}

    def add_dragon(self, dragon: Dragon):
        if dragon.type not in self.repository:
            self.repository[dragon.type] = {}

        self.repository[dragon.type][dragon.name] = {"damage": int(dragon.damage),
        "health": int(dragon.health), "armor": int(dragon.armor)}

def read_input(n):
    result = []

    for _ in range(n):
        result.append(input())

    return result

def create_and_add_dragons_to_collector(data):
    dragon_collector = DragonCollector()

    for line in data:
        type, name, damage, health, armor = line.split()
        dragon_collector.add_dragon(Dragon(type, name, damage, health, armor))

    return dragon_collector

def get_average_points_by_value_type(dragons, value):
    total_points = 0
    for values in dragons.values():
        total_points += values[value]

    return total_points / len(dragons)

def print_result(repository):
    for dragon_type, dragons in repository.items():
        sorted_dragons = dict(sorted(dragons.items()))
        average_damage = get_average_points_by_value_type(dragons, "damage")
        average_health = get_average_points_by_value_type(dragons, "health")
        average_armor = get_average_points_by_value_type(dragons, "armor")
        print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
        for dragon, values in sorted_dragons.items():
            print(f"-{dragon} -> damage: {values['damage']}, "
                  f"health: {values['health']}, armor: {values['armor']}")

n = int(input()) # num of dragons
input_data = read_input(n)
dragon_collector = create_and_add_dragons_to_collector(input_data)
print_result(dragon_collector.repository)

