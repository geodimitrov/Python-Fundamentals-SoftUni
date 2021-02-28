
items = input().split("|")
budget = float(input())
total_cost = 0
bought_items = []


for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes" and item_price > 50.00:
        continue
    if item_type == "Shoes" and item_price > 35.00:
        continue
    if item_type == "Accessories" and item_price > 20.50:
        continue
        
    if budget >= item_price:
        budget -= item_price
        total_cost += item_price
        bought_items.append(item_price * 1.4)

profit = sum(bought_items) - total_cost
budget += sum(bought_items)

for el in bought_items:
    print(f"{el:.2f} ", end="")
    
print()
print (f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

