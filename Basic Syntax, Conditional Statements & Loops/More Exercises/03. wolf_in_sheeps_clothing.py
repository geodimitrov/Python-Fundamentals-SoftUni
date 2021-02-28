
# read input and turn it into list
animals = input().split(", ")
WOLF = "wolf" # it just looks more pythonic this way

# create conditions
if animals[-1] == WOLF:
    print("Please go away and stop eating my sheep")
else:
    #find the sheep's position by locating the wolf
    for i in range(len(animals) - 1, -1, -1):
        if animals[i] == WOLF:
            sheep_position = len(animals) - (abs(i) + 1)
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
