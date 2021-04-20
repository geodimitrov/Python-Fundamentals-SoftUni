energy = int(input())

command = input()
won_battles = 0
enough_energy = True

while not command == "End of battle":

    if int(command) > energy:
        enough_energy = False
        break
    else:
        energy -= int(command)
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles

    command = input()

if enough_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")