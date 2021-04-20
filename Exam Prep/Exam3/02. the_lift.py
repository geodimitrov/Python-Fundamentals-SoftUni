n_people = int(input())

lift = [int(el) for el in input().split()]
MAX_CAPACITY = 4

for index in range(len(lift)):
    while lift[index] < MAX_CAPACITY:
        if n_people > 0:
            lift[index] += 1
            n_people -= 1
        else:
            break

result = " ".join([str(el) for el in lift])

if n_people > 0 and lift[-1] == MAX_CAPACITY:
    print(f"There isn't enough space! {n_people} people in a queue!")
elif n_people == 0 and lift[-1] < MAX_CAPACITY:
    print("The lift has empty spots!")

print(result)