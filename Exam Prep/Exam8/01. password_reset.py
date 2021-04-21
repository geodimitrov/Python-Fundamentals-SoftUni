END_COMMAND = "Done"
string = input()

while True:
    command = input()

    if command == END_COMMAND:
        break

    if command == "TakeOdd":
        result = ""
        for i in range(len(string)):
            if i % 2 != 0:
                result += string[i]
        string = result
        print(string)

    elif command.startswith("Cut"):
        index = int(command.split()[1])
        length = int(command.split()[2])
        substring = string[index:index + length]
        string = string.replace(substring, "", 1)
        print(string)

    else:
        substring, substitute = command.split()[1:]
        if substring not in string:
            print("Nothing to replace!")
        else:
            string = string.replace(substring, substitute)
            print(string)

print(f"Your password is: {string}")
