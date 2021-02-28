
# Introduce data, split and run list comprehension to turn el into ints
houses_data = [int(el) for el in input().split("@")]
house_i = 0

# Start making "jumps" by receiving commands until you get "Love!"
command = input()

while not command == "Love!":
    length =  int(command.split()[1]) #the length of the jump will always be the 2nd el of the command, make it int
    house_i += length
    
    # if the jump exceeds the range of the houses, start from 0
    if house_i > len(houses_data) - 1:
        house_i = 0
    
    if houses_data[house_i] == 0:
        print(f"Place {house_i} already had Valentine's day.")
    else:
        houses_data[house_i] -= 2
        if houses_data[house_i] == 0:
            print(f"Place {house_i} has Valentine's day.")
    
    command = input()
    
print(f"Cupid's last position was {house_i}.")

if sum(houses_data) == 0:
    print("Mission was successful.")
else:
    failed_houses = [el for el in houses_data if el > 0]
    print(f"Cupid has failed {len(failed_houses)} places.")
