message = input()

operation = input()

while not operation == "Decode":
    command = operation.split("|")[0]

    if command == "Move":
        n_letters = int(operation.split("|")[1])
        add_letter = message[:n_letters]
        message = message[n_letters:] + add_letter

    elif command == "Insert":
        index = int(operation.split("|")[1])
        value = operation.split("|")[2]
        message = message[:index] + value + message[index:]

    elif command == "ChangeAll":
        substring, replacement = operation.split("|")[1:]
        message = message.replace(substring, replacement)

    operation = input()

print(f"The decrypted message is: {message}")