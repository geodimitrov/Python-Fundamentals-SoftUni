data = input()

command = input()

while not command == "Travel":
    command_type = command.split(":")[0]

    if command_type == "Add Stop":
        index = int(command.split(":")[1])
        string = command.split(":")[2]
        if index in range(len(data)):
            data = data[:index] + string + data[index:]
        print(data)

    elif command_type == "Remove Stop":
        start_index = int(command.split(":")[1])
        end_index = int(command.split(":")[2])
        if start_index in range(len(data)) and end_index in range(len(data)):
            data = data[:start_index] + data[end_index + 1:]
        print(data)

    elif command_type == "Switch":
        old_string, new_string = command.split(":")[1:]
        if old_string in data:
            data = data.replace(old_string, new_string)
        print(data)

    command = input()

print(f"Ready for world tour! Planned stops: {data}")