n = int(input())

data = {}

for _ in range(n):
    piece_name, composer, key = input().split("|")
    data[piece_name] = [composer, key]

command = input()

while not command == "Stop":
    command_type = command.split("|")[0]

    if command_type == "Add":
        piece, composer, key = command.split("|")[1:]
        if piece not in data:
            data[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command_type == "Remove":
        piece = command.split("|")[1]
        if piece not in data:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del data[piece]
            print(f"Successfully removed {piece}!")

    elif command_type == "ChangeKey":
        piece, new_key = command.split("|")[1:]
        if piece not in data:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            data[piece][-1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

sorted_data = dict(sorted(data.items()))

for key, value in sorted_data.items():
    print (f"{key} -> Composer: {value[0]}, Key: {value[1]}")