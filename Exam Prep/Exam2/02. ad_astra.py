import re

data = input()

pattern = r"([#\|])(?P<item>[a-zA-Z\s]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"

valid_data = re.finditer(pattern, data)
food_data = []
total_calories = 0
calories_per_day = 2000

for match in valid_data:
    food_data.append(match.groupdict())
    calories = int(match["calories"])
    total_calories += calories

print(f"You have food to last you for: {total_calories // calories_per_day} days!")
for el in food_data:
    print(f"Item: {el['item']}, Best before: {el['exp_date']}, Nutrition: {el['calories']}")