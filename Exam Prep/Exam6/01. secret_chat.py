message = input()

command = input()

while not command == "Reveal":
    command_type = command.split(":|:")[0]

    if command_type == "InsertSpace":
        index = int(command.split(":|:")[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif command_type == "Reverse":
        substring = command.split(":|:")[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")

    elif command_type == "ChangeAll":
        substring, replacement = command.split(":|:")[1:]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")