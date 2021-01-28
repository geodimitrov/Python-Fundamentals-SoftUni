from itertools import combinations

def chair_combinations(names, n_chairs):
    return combinations(names, n_chairs)

names = input().split(", ")
n = int(input()) #num of chairs
[print(*el, sep=", ") for el in chair_combinations(names, n)]