list_items = input().split("!")

command = input()

while not command == "Go Shopping!":
    command_type = command.split()[0]
    item = command.split()[1]

    if command_type == "Urgent" and not item in list_items:
        list_items.insert(0, item)

    elif command_type == "Unnecessary" and item in list_items:
        list_items.remove(item)

    elif command_type == "Correct" and item in list_items:
        new_item = command.split()[2]
        item_index = list_items.index(item)
        list_items[item_index] = new_item

    elif command_type == "Rearrange" and item in list_items:
        list_items.remove(item)
        list_items.append(item)

    command = input()

print(", ".join(list_items))