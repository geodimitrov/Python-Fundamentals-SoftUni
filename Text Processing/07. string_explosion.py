EXPLOSION = ">"
string = [el for el in input()]
i = 0
explosion_strength = 0

while i < len(string):
    char = string[i]

    if char == EXPLOSION:
        explosion_strength += int(string[i + 1])
        curr_index = i + 1

        if curr_index not in range(len(string)):
            break

        while True:
            if curr_index not in range(len(string)):
                break

            if explosion_strength == 0 or string[curr_index] == EXPLOSION:
                break
            else:
                string.pop(curr_index)
                explosion_strength -= 1

    i += 1

print("".join(string))