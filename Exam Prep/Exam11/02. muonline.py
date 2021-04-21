data = input().split("|")
health = 100
bitcoins = 0
dead = False
cell_counter = 0

for cell in data:
    command = cell.split()[0]
    number = int(cell.split()[1])
    cell_counter += 1

    if command == "potion":
        if health + number > 100:
            heal_amount = 100 - health
            health = 100
        else:
            health += number
            heal_amount = number
        print(f"You healed for {heal_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {cell_counter}")
            dead = True
        else:
            print(f"You slayed {command}.")

    if dead:
        break

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")