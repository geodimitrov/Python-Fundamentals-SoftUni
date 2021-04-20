import re

data = input()

ex = r"(?<=([=/]))([A-Z][a-zA-Z]{2,})(?=\1)"

valid_locations = [match.group() for match in re.finditer(ex, data)]
points = 0

for location in valid_locations:
    points += len(location)

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {points}")