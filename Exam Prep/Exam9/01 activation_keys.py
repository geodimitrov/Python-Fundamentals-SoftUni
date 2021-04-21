key = input()

command = input()

while not command == "Generate":
    command_type = command.split(">>>")[0]

    if command_type == "Contains":
        substring = command.split(">>>")[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command_type == "Flip":
        letter_case, i_start, i_end = command.split(">>>")[1:4]
        i_start, i_end = int(i_start), int(i_end)
        if letter_case == "Upper":
            key = key.replace(key[i_start:i_end], key[i_start:i_end].upper())
        elif letter_case == "Lower":
            key = key.replace(key[i_start:i_end], key[i_start:i_end].lower())
        print(key)

    elif command_type == "Slice":
        i_start, i_end = command.split(">>>")[1:]
        i_start, i_end = int(i_start), int(i_end)
        key = key.replace(key[i_start:i_end], "")
        print(key)

    command = input()

print(f"Your activation key is: {key}")