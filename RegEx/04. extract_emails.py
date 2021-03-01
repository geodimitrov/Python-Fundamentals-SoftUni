import re

data = input()

ex = r"(^|(?<=\s))([a-zA-Z0-9][\._-]?)+@[a-z]+-?[a-z]+(\.[a-z]+-?)+"

matches = [match.group() for match in re.finditer(ex, data)]

for match in matches:
    print(match)