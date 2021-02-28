# 1. Create input (they don't specify whether "int" or "float" so we'll stick with "int")
age = int(input())


# 2. Create conditions
if age <= 14:
    drink_type = "toddy"
elif 14 < age <= 18:
    drink_type = "coke"
elif 18 < age <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"

# 3. Print result    
print(f"drink {drink_type}")