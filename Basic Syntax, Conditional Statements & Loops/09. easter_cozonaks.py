# 1. Introduce variables
budget = float(input())
price_flour = float(input())
colored_eggs = 0
cozonaks = 0

# 2. Calculate price of eggs, milk & cozonak
price_eggs = price_flour * 0.75
price_milk_lt = price_flour * 1.25 #we will use 0.250 l per cozonak
price_cozonak = price_flour + price_eggs + price_milk_lt * 0.25

# 3. Use while loop to calculate N of cozonaks you made + colored eggs and how much you've got left
while budget >= price_cozonak:
    cozonaks += 1
    colored_eggs += 3
    if cozonaks % 3 == 0:
        colored_eggs -= cozonaks - 2
    budget -= price_cozonak
    
# 4. Print the results
print (f"You made {cozonaks} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")