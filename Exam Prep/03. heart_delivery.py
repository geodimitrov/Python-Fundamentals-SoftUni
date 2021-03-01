houses = [int(house) for house in input().split("@")]

command = input()
position = 0

while not command == "Love!":

    position += int(command.split()[1])
    if position > len(houses) - 1:
        position = 0

    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

if sum(houses) == 0:
    print("Mission was successful.")
else:
    counter = len([el for el in houses if el > 0])
    print(f"Cupid has failed {counter} places.")