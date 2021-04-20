targets = [int(el) for el in input().split()]

command = input()

while not command == "End":
    i_target = int(command)

    if not i_target in range(len(targets)):
        command = input()
        continue

    target_value = targets[i_target]

    if not targets[i_target] == -1:
        targets[i_target] = -1

    for i in range(len(targets)):
        i_value = targets[i]
        if not i_value == -1 and i_value > target_value:
            i_value -= target_value
            targets[i] = i_value
        elif not i_value == -1 and i_value <= target_value:
            i_value += target_value
            targets[i] = i_value

    command = input()

shot_targets = len([el for el in targets if el == -1])
target_values = " ".join([str(el) for el in targets])

print(f"Shot targets: {shot_targets} -> {target_values}")