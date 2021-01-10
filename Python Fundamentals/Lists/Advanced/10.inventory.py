
#receive input data and split to turn it into list
items = input().split(", ")

# start receiving commands until "Craft!"
command = input()

while not command == "Craft!":
    command_type, value = command.split(" - ")
    
    if command_type == "Collect":
        item = value
        if item not in items:
            items.append(item)
        
    elif command_type == "Drop":
        item = value
        if item in items:
            items.remove(item)
            
    elif command_type == "Combine Items":
        old_item, new_item = value.split(":")
        if old_item in items:
            index = items.index(old_item)
            items.insert(index+1, new_item)
             
    elif command_type == "Renew":
        item = value
        if item in items:
            items.remove(item)
            items.append(item)
    
    command = input()

# unpack the list and use ", " as a separator, print it
print(*items, sep=", ")
