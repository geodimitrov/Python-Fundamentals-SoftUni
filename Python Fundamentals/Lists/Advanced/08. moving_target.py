#!/usr/bin/env python
# coding: utf-8

# In[ ]:


targets = [int(el) for el in input().split()]

command = input()

while not command == "End":
    command_type = command.split()[0]
    index = int(command.split()[1])

    if command_type == "Shoot":
        power = int(command.split()[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif command_type == "Add":
        target_value = int(command.split()[2])
        if index in range(len(targets)):
            targets.insert(index, target_value)
        else:
            print("Invalid placement!")

    elif command_type == "Strike":
        radius = int(command.split()[2])

        if index + radius in range(len(targets)) and index - radius in range(len(targets)):
            targets = targets[:index - radius] + targets[index + radius + 1:]
        else:
            print("Strike missed!")

    command = input()

targets = [str(t) for t in targets]

print("|".join(targets))

