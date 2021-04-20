array_values = [int(el) for el in input().split()]

command = input().split()

while not "end" in command:

    if "decrease" in command:
        array_values = [el - 1 for el in array_values]

    else:
        index_1 = int(command[1])
        index_2 = int(command[2])

        if "swap" in command:
            array_values[index_1], array_values[index_2] = array_values[index_2], array_values[index_1]

        elif "multiply" in command:
            array_values[index_1] *= array_values[index_2]

    command = input().split()

new_array = ", ".join([str(el) for el in array_values])
print(new_array)