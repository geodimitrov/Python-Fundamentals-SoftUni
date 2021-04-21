class Hero:
    max_mana_points = 200
    max_hit_points = 100

    def __init__(self, name, hit_points, mana_points):
        self.name = name
        self.hit_points = hit_points
        self.mana_points = mana_points
        self.is_alive = True

    def cast_spell(self, mp, spell):
        if self.mana_points < mp:
            print(f"{self.name} does not have enough MP to cast {spell}!")
            return
        self.mana_points -= mp
        print(f"{self.name} has successfully cast {spell} and now has {self.mana_points} MP!")

    def take_damage(self, damage, attacker):
        if self.hit_points <= damage:
            self.is_alive = False
            print(f"{self.name} has been killed by {attacker}!")
            return

        self.hit_points -= damage
        print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hit_points} HP left!")

    def recharge(self, mp_amount):
        if self.mana_points + mp_amount >= self.max_mana_points:
            mp_amount = self.max_mana_points - self.mana_points
        self.mana_points += mp_amount
        print(f"{self.name} recharged for {mp_amount} MP!")

    def heal(self, hp_amount):
        if self.hit_points + hp_amount >= self.max_hit_points:
            hp_amount = self.max_hit_points - self.hit_points
        self.hit_points += hp_amount
        print(f"{self.name} healed for {hp_amount} HP!")

def create_heroes(n):
    result = []

    for _ in range(n):
        name, hp, mp = input().split()
        result.append(Hero(name, int(hp), int(mp)))
    return result

def read_commands():
    result = []

    while True:

        command = input()

        if command == "End":
            break
        result.append(command)

    return result

def execute_command(command, heroes):

    if command.startswith("CastSpell"):
        hero_name, mp_needed, spell_name = command.split(" - ")[1:]
        hero = [obj for obj in heroes if obj.name == hero_name][0]
        hero.cast_spell(int(mp_needed), spell_name)

    elif command.startswith("TakeDamage"):
        hero_name, damage, attacker = command.split(" - ")[1:]
        hero = [obj for obj in heroes if obj.name == hero_name][0]
        hero.take_damage(int(damage), attacker)

        if not hero.is_alive:
            heroes.remove(hero)

    elif command.startswith("Recharge"):
        hero_name, amount = command.split(" - ")[1:]
        hero = [obj for obj in heroes if obj.name == hero_name][0]
        hero.recharge(int(amount))

    else:
        hero_name, amount = command.split(" - ")[1:]
        hero = [obj for obj in heroes if obj.name == hero_name][0]
        hero.heal(int(amount))

def format_result(heroes):
    result = {f"{hero.name}": [hero.hit_points, hero.mana_points]
              for hero in heroes
            }

    sorted_result = dict(sorted(result.items(), key=lambda x: (-x[1][0], x[0])))
    return sorted_result

def print_result(result):
    for hero_name, values in result.items():
        print(f"{hero_name}\n  HP: {values[0]}\n  MP: {values[1]}")

n = int(input())
heroes = create_heroes(n)
commands = read_commands()

for command in commands:
    execute_command(command, heroes)

formatted_result = format_result(heroes)
print_result(formatted_result)