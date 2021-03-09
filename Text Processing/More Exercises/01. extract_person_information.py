import re

NAME_SEPARATOR = "[@|]"
AGE_SEPARATOR = "[#*]"

def read_input(n):
    result = []
    for line in range(n):
        result.append(input())
    return result

N = int(input()) # num of lines
input_data = read_input(N)
for string in input_data:
    name = re.split(NAME_SEPARATOR, string)[1]
    age = re.split(AGE_SEPARATOR, string)[1]
    print(f"{name} is {age} years old.")