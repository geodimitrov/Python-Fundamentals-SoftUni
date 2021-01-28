from itertools import permutations

def text_permutation(string):
    return list(permutations(string))

text = input()
[print("".join(el)) for el in text_permutation(text)]