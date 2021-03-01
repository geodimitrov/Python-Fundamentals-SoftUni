current_version = [int(el) for el in input().split(".")]

for i in range(len(current_version) -1, -1, -1):
    if current_version[i] < 9:
        current_version[i] += 1
        break
    else:
        current_version[i] = 0
        continue

new_version = ".".join([str(el) for el in current_version])

print(new_version)