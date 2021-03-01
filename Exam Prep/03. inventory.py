items = input().split(", ")

command = input()

while not command == "Craft!":
    command_type = command.split(" - ")[0]
    item = command.split(" - ")[1]

    if command_type == "Collect":
        if not item in items:
            items.append(item)

    elif command_type == "Drop":
        if item in items:
            items.remove(item)

    elif command_type == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)

    elif command_type == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)

    command = input()

print(", ".join(items))